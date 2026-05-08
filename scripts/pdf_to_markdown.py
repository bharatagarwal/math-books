# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "mistralai>=1.2.0",
#     "tqdm>=4.66.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""Convert PDFs to markdown via Mistral OCR.

Idempotent: skips PDFs that already have a corresponding .md output.
Loads MISTRAL_API_KEY from scripts/.env if present.
Run: `uv run scripts/pdf_to_markdown.py path/to/file.pdf [more.pdf ...]`
Or to process every PDF in the repo: `uv run scripts/pdf_to_markdown.py --all`
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from dotenv import load_dotenv
from mistralai.client.sdk import Mistral
from tqdm import tqdm

load_dotenv(Path(__file__).resolve().parent / ".env")

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = REPO_ROOT / "markdown"
MODEL = "mistral-ocr-latest"
RENDER_DPI = 300  # local pdftoppm render DPI for lossless image extraction


def output_path_for(pdf: Path) -> Path:
    rel = pdf.resolve().relative_to(REPO_ROOT)
    return (OUTPUT_ROOT / rel).with_suffix(".md")


def images_dir_for(pdf: Path) -> Path:
    md = output_path_for(pdf)
    return md.with_name(f"{md.stem}_images")


def manifest_path_for(pdf: Path) -> Path:
    return output_path_for(pdf).with_suffix(".manifest.json")


def already_done(pdf: Path) -> bool:
    md = output_path_for(pdf)
    manifest = manifest_path_for(pdf)
    if not (md.exists() and manifest.exists()):
        return False
    try:
        meta = json.loads(manifest.read_text())
    except json.JSONDecodeError:
        return False
    return meta.get("source_size") == pdf.stat().st_size and meta.get("model") == MODEL


def ocr_pdf(client: Mistral, pdf: Path) -> dict:
    with pdf.open("rb") as f:
        uploaded = client.files.upload(
            file={"file_name": pdf.name, "content": f},
            purpose="ocr",
        )
    try:
        signed = client.files.get_signed_url(file_id=uploaded.id)
        response = client.ocr.process(
            model=MODEL,
            document={"type": "document_url", "document_url": signed.url},
            include_image_base64=False,
        )
    finally:
        try:
            client.files.delete(file_id=uploaded.id)
        except Exception:
            pass
    return response.model_dump() if hasattr(response, "model_dump") else dict(response)


def render_page(pdf: Path, page_num: int, output: Path, dpi: int = RENDER_DPI) -> bool:
    """Render a single PDF page to PNG via pdftoppm. Returns True on success."""
    with tempfile.TemporaryDirectory() as tmp:
        prefix = Path(tmp) / "render"
        subprocess.run(
            [
                "pdftoppm", "-png", "-r", str(dpi),
                "-f", str(page_num), "-l", str(page_num),
                str(pdf), str(prefix),
            ],
            check=True, capture_output=True,
        )
        rendered = list(Path(tmp).glob("render-*.png"))
        if not rendered:
            return False
        rendered[0].rename(output)
        return True


def crop_bbox(render_path: Path, bbox: tuple[int, int, int, int], scale: float, output: Path) -> None:
    """Crop bbox from rendered page using ImageMagick. Output format inferred from suffix."""
    x1, y1, x2, y2 = (int(v * scale) for v in bbox)
    w, h = max(1, x2 - x1), max(1, y2 - y1)
    subprocess.run(
        ["magick", str(render_path), "-crop", f"{w}x{h}+{x1}+{y1}", "+repage", str(output)],
        check=True, capture_output=True,
    )


def write_outputs(pdf: Path, response: dict) -> None:
    md_path = output_path_for(pdf)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    img_dir = images_dir_for(pdf)
    img_prefix = img_dir.name

    pages = response.get("pages", [])
    image_count = 0
    parts = []

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        for i, page in enumerate(pages, start=1):
            markdown = page.get("markdown", "")
            images = page.get("images") or []

            if images:
                img_dir.mkdir(parents=True, exist_ok=True)
                dims = page.get("dimensions") or {}
                mistral_dpi = dims.get("dpi") or 200
                scale = RENDER_DPI / mistral_dpi

                rendered = tmp_dir / f"page-{i:04d}.png"
                if not render_page(pdf, i, rendered, RENDER_DPI):
                    tqdm.write(f"warning: render failed for {pdf.name} page {i}")
                else:
                    for image in images:
                        bbox = (
                            image["top_left_x"], image["top_left_y"],
                            image["bottom_right_x"], image["bottom_right_y"],
                        )
                        if any(v is None for v in bbox):
                            continue
                        out = img_dir / image["id"]
                        try:
                            crop_bbox(rendered, bbox, scale, out)
                            markdown = markdown.replace(
                                f"]({image['id']})", f"]({img_prefix}/{image['id']})"
                            )
                            image_count += 1
                        except subprocess.CalledProcessError as e:
                            tqdm.write(f"warning: crop failed {pdf.name} p{i} {image['id']}: {e}")

            parts.append(f"<!-- page {i} -->\n\n{markdown}")

    md_path.write_text("\n\n---\n\n".join(parts))

    manifest_path_for(pdf).write_text(
        json.dumps(
            {
                "source": str(pdf.relative_to(REPO_ROOT)),
                "source_size": pdf.stat().st_size,
                "model": MODEL,
                "pages": len(pages),
                "images": image_count,
                "render_dpi": RENDER_DPI,
                "usage": response.get("usage_info"),
            },
            indent=2,
        )
    )


def collect_pdfs(args: argparse.Namespace) -> list[Path]:
    if args.all:
        return sorted(REPO_ROOT.rglob("*.pdf"))
    found: list[Path] = []
    for p in args.pdfs:
        path = Path(p).resolve()
        if path.is_dir():
            found.extend(sorted(path.rglob("*.pdf")))
        elif path.is_file():
            found.append(path)
        else:
            print(f"warning: {p} not found, skipping", file=sys.stderr)
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdfs", nargs="*", help="PDF paths to process")
    parser.add_argument("--all", action="store_true", help="Process every PDF under the repo")
    parser.add_argument("--force", action="store_true", help="Re-process even if output exists")
    args = parser.parse_args()

    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("error: MISTRAL_API_KEY env var not set", file=sys.stderr)
        return 2

    pdfs = collect_pdfs(args)
    if not pdfs:
        parser.print_help()
        return 1

    client = Mistral(api_key=api_key)

    todo = pdfs if args.force else [p for p in pdfs if not already_done(p)]
    skipped = len(pdfs) - len(todo)
    if skipped:
        print(f"skipping {skipped} already-processed PDF(s)")

    failures: list[tuple[Path, str]] = []
    for pdf in tqdm(todo, desc="OCR", unit="pdf"):
        try:
            response = ocr_pdf(client, pdf)
            write_outputs(pdf, response)
        except Exception as exc:
            failures.append((pdf, str(exc)))
            tqdm.write(f"failed: {pdf.name}: {exc}")

    if failures:
        print(f"\n{len(failures)} failure(s):")
        for pdf, err in failures:
            print(f"  {pdf}: {err}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
