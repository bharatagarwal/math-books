#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Extract code blocks from markdown to separate files, and inline them back.

Commands:
    extract <markdown_file>  - Extract code blocks to files, replace with include directives
    build <markdown_file>    - Inline includes back into markdown for reading
    list <markdown_file>     - Show code blocks that would be extracted

Include directive format:
    <!-- include: path/to/file.py -->

Extracted files go to: code/<book>/<chapter>/01_<lang>.<ext>
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CODE_DIR = REPO_ROOT / "code"
MARKDOWN_DIR = REPO_ROOT / "markdown"

LANG_EXT = {
    "python": "py",
    "py": "py",
    "lean": "lean",
    "lean4": "lean",
    "dafny": "dfy",
    "javascript": "js",
    "js": "js",
    "typescript": "ts",
    "ts": "ts",
    "bash": "sh",
    "sh": "sh",
    "shell": "sh",
    "z3": "py",  # Z3 is usually Python
}

CODE_BLOCK_RE = re.compile(
    r'^```(\w+)?\n(.*?)^```',
    re.MULTILINE | re.DOTALL
)

INCLUDE_RE = re.compile(
    r'^<!-- include: (.+?) -->$',
    re.MULTILINE
)


def get_code_dir(md_path: Path) -> Path:
    """Map markdown path to code directory."""
    md_path = md_path.resolve()
    try:
        rel = md_path.relative_to(MARKDOWN_DIR)
    except ValueError:
        rel = Path(md_path.stem)

    # Remove .md extension for the directory name
    if rel.suffix == ".md":
        rel = rel.with_suffix("")

    return CODE_DIR / rel


def extract_blocks(content: str) -> list[tuple[str, str, int, int]]:
    """Extract code blocks from markdown content.

    Returns: [(lang, code, start_pos, end_pos), ...]
    """
    blocks = []
    for match in CODE_BLOCK_RE.finditer(content):
        lang = match.group(1) or "txt"
        code = match.group(2)
        blocks.append((lang, code, match.start(), match.end()))
    return blocks


def should_extract(code: str, lang: str) -> bool:
    """Decide if a code block should be extracted to a file.

    Skip very short blocks (< 3 lines) that are just output examples.
    """
    lines = [l for l in code.strip().split("\n") if l.strip()]
    if len(lines) < 3:
        return False
    # Skip blocks that look like output only
    if all(l.startswith("#") or l.startswith("//") for l in lines):
        return False
    return True


def extract(md_path: Path, dry_run: bool = False) -> None:
    """Extract code blocks from markdown to separate files."""
    content = md_path.read_text()
    blocks = extract_blocks(content)

    if not blocks:
        print(f"No code blocks found in {md_path}")
        return

    code_dir = get_code_dir(md_path)

    # Track replacements (process in reverse to preserve positions)
    replacements = []
    file_counter = {}  # Track per-language counters

    for lang, code, start, end in blocks:
        if not should_extract(code, lang):
            continue

        ext = LANG_EXT.get(lang.lower(), lang.lower())

        # Increment counter for this language
        file_counter[ext] = file_counter.get(ext, 0) + 1
        idx = file_counter[ext]

        filename = f"{idx:02d}_{lang}.{ext}"
        rel_path = code_dir.relative_to(REPO_ROOT) / filename

        include_directive = f"<!-- include: {rel_path} -->"

        replacements.append((start, end, include_directive, code_dir / filename, code, lang))

    if not replacements:
        print(f"No extractable code blocks in {md_path}")
        return

    if dry_run:
        print(f"\nWould extract from {md_path}:")
        for _, _, directive, file_path, code, lang in replacements:
            lines = len(code.strip().split("\n"))
            print(f"  {file_path.name} ({lang}, {lines} lines)")
        return

    # Create code directory
    code_dir.mkdir(parents=True, exist_ok=True)

    # Write code files
    for _, _, _, file_path, code, _ in replacements:
        file_path.write_text(code)
        print(f"  Wrote {file_path}")

    # Replace blocks in markdown (reverse order to preserve positions)
    new_content = content
    for start, end, directive, _, _, lang in reversed(replacements):
        # Keep the language hint for build step
        new_content = new_content[:start] + f"```{lang}\n{directive}\n```" + new_content[end:]

    md_path.write_text(new_content)
    print(f"Updated {md_path} with {len(replacements)} include directives")


def build(md_path: Path, output: Path | None = None) -> None:
    """Inline include directives back into markdown."""
    content = md_path.read_text()

    def replace_include(match: re.Match) -> str:
        rel_path = match.group(1)
        file_path = REPO_ROOT / rel_path
        if file_path.exists():
            return file_path.read_text().rstrip("\n")
        else:
            return f"# ERROR: File not found: {rel_path}"

    new_content = INCLUDE_RE.sub(replace_include, content)

    if output:
        output.write_text(new_content)
        print(f"Built {output}")
    else:
        print(new_content)


def list_blocks(md_path: Path) -> None:
    """List code blocks in a markdown file."""
    content = md_path.read_text()
    blocks = extract_blocks(content)

    print(f"\nCode blocks in {md_path}:")
    for i, (lang, code, _, _) in enumerate(blocks, 1):
        lines = len(code.strip().split("\n"))
        extractable = "✓" if should_extract(code, lang) else "·"
        first_line = code.strip().split("\n")[0][:60]
        print(f"  {extractable} {i:2d}. [{lang:10s}] {lines:3d} lines | {first_line}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    # extract command
    extract_parser = subparsers.add_parser("extract", help="Extract code blocks to files")
    extract_parser.add_argument("file", type=Path, help="Markdown file to process")
    extract_parser.add_argument("--dry-run", "-n", action="store_true", help="Show what would be extracted")

    # build command
    build_parser = subparsers.add_parser("build", help="Inline includes back into markdown")
    build_parser.add_argument("file", type=Path, help="Markdown file to process")
    build_parser.add_argument("--output", "-o", type=Path, help="Output file (default: stdout)")

    # list command
    list_parser = subparsers.add_parser("list", help="List code blocks in file")
    list_parser.add_argument("file", type=Path, help="Markdown file to inspect")

    args = parser.parse_args()

    if not args.file.exists():
        print(f"Error: {args.file} not found", file=sys.stderr)
        sys.exit(1)

    if args.command == "extract":
        extract(args.file, dry_run=args.dry_run)
    elif args.command == "build":
        build(args.file, args.output)
    elif args.command == "list":
        list_blocks(args.file)


if __name__ == "__main__":
    main()
