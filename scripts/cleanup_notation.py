#!/usr/bin/env python3
"""Clean up OCR artifacts in mathematical-notation markdown files.

Pass 2: Remove running page headers (chapter titles as bare lines mid-content).
"""

import re
from pathlib import Path

MD_DIR = Path("markdown/mathematical-notation")

CHAPTER_TITLES = {
    '00 - Preface.md': 'Preface',
    '01 - Letters.md': 'Letters',
    '02 - Collections.md': 'Collections',
    '03 - Logic.md': 'Logic',
    '04 - Numbers.md': 'Numbers',
    '05 - Geometry.md': 'Geometry',
    '06 - Functions.md': 'Functions',
    '07 - Linear Algebra.md': 'Linear Algebra',
    '08 - Calculus.md': 'Calculus',
    '09 - Probability and Statistics.md': 'Probability and Statistics',
    '10 - Approximation.md': 'Approximation',
}


def clean_file(path: Path) -> str:
    name = path.name
    title = CHAPTER_TITLES.get(name)
    if not title:
        return path.read_text()

    lines = path.read_text().split('\n')
    cleaned = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip bare chapter-title lines that are page headers (not the H1 title)
        if stripped == title and i > 0:
            # Make sure this isn't part of a heading
            if i > 0 and not lines[i-1].strip().startswith('#'):
                continue
        cleaned.append(line)

    text = '\n'.join(cleaned)
    # Collapse excessive blank lines
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = text.strip() + '\n'
    return text


def main():
    for f in sorted(MD_DIR.glob('*.md')):
        original = f.read_text()
        cleaned = clean_file(f)
        if cleaned != original:
            f.write_text(cleaned)
            delta = len(original.split('\n')) - len(cleaned.split('\n'))
            print(f"  {f.name}: removed {delta} header lines")
        else:
            print(f"  {f.name}: no changes")


if __name__ == '__main__':
    main()
