# /// script
# requires-python = ">=3.10"
# ///
"""Lint Markdown prose paragraphs that exceed a character budget.

A "prose paragraph" is a blank-line-separated block of running text. The
following block types are NEVER prose and are skipped (never flagged, never to
be split): headings, list items, blockquotes, tables, fenced code, display-math
($$ ... $$), figure/image lines, HTML comments / include / carousel directives,
horizontal rules, and raw HTML blocks. Code fences and $$-blocks are tracked
across lines so their interiors are never mistaken for prose.

Usage:
  uv run scripts/pim_para_lint.py [PATHS...] [--limit N] [--verify] [--quiet]

  PATHS    files and/or directories (dirs scanned for *.md). Default: cwd.
  --limit  character budget per paragraph (default 500).
  --verify exit 1 if any prose paragraph exceeds the budget (for CI/checks).
  --quiet  print only the per-file/over-limit summary, not each offender.
"""
from __future__ import annotations

import re
import sys
import pathlib

FENCE = re.compile(r"^\s{0,3}(```|~~~)")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
LISTITEM = re.compile(r"^\s*([-*+]\s|\d+[.)]\s)")
BLOCKQUOTE = re.compile(r"^\s*>")
TABLEROW = re.compile(r"^\s*\|")
IMAGE = re.compile(r"^\s*!\[")
COMMENT = re.compile(r"^\s*<!--")
HTML = re.compile(r"^\s*<[a-zA-Z/!]")
HR = re.compile(r"^\s*([-*_])\s*(\1\s*){2,}$")
MATH_OPEN = re.compile(r"^\s*\$\$")


def _is_nonprose(first: str) -> bool:
    return bool(
        HEADING.match(first)
        or LISTITEM.match(first)
        or BLOCKQUOTE.match(first)
        or TABLEROW.match(first)
        or IMAGE.match(first)
        or COMMENT.match(first)
        or HR.match(first)
        or MATH_OPEN.match(first)
        or HTML.match(first)
    )


def find_offenders(path: pathlib.Path, limit: int) -> list[tuple[int, int, str]]:
    """Return (1-based start line, char length, preview) per over-limit prose para."""
    lines = path.read_text(encoding="utf-8").split("\n")
    n = len(lines)
    out: list[tuple[int, int, str]] = []
    block: list[str] = []
    start = 0

    def flush() -> None:
        if not block:
            return
        text = "\n".join(block)
        if not _is_nonprose(block[0]) and len(text) > limit:
            preview = text[:90].replace("\n", " ")
            out.append((start + 1, len(text), preview))

    i = 0
    while i < n:
        line = lines[i]
        ls = line.lstrip()
        # fenced code block: skip its whole span
        if FENCE.match(line):
            flush()
            block = []
            marker = "```" if ls.startswith("```") else "~~~"
            i += 1
            while i < n and not lines[i].lstrip().startswith(marker):
                i += 1
            i += 1
            continue
        # display-math block delimited by a lone $$ line: skip its span
        if line.strip() == "$$":
            flush()
            block = []
            i += 1
            while i < n and lines[i].strip() != "$$":
                i += 1
            i += 1
            continue
        if line.strip() == "":
            flush()
            block = []
            i += 1
            continue
        if not block:
            start = i
        block.append(line)
        i += 1
    flush()
    return out


def iter_md(paths: list[str]) -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for p in paths:
        pp = pathlib.Path(p)
        if pp.is_dir():
            files.extend(sorted(pp.rglob("*.md")))
        elif pp.suffix == ".md":
            files.append(pp)
    return files


def main() -> int:
    args = sys.argv[1:]
    limit = 500
    verify = "--verify" in args
    quiet = "--quiet" in args
    if "--limit" in args:
        idx = args.index("--limit")
        limit = int(args[idx + 1])
        del args[idx : idx + 2]
    paths = [a for a in args if not a.startswith("--")] or ["."]

    files = iter_md(paths)
    total = 0
    for f in files:
        offenders = find_offenders(f, limit)
        if not offenders:
            continue
        total += len(offenders)
        print(f"\n{f}  ({len(offenders)} over {limit})")
        if not quiet:
            for ln, length, preview in offenders:
                print(f"  L{ln:<5} {length:>5} chars  {preview}…")

    print(f"\n{'=' * 60}")
    print(f"{total} prose paragraph(s) over {limit} chars across {len(files)} file(s).")
    if verify:
        return 1 if total else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
