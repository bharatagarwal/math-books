# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Clean up OCR'd markdown files from MCS textbook.

Fixes:
- Remove "Chapter N Title" header/footer lines
- Remove duplicate section headers (page headers)
- Convert HTML entities to characters
- Normalize heading hierarchy (## for sections, ### for subsections)
- Remove stray horizontal rules
- Remove page numbers
- Fix common LaTeX issues
"""
import re
import sys
from pathlib import Path


def clean_markdown(content: str) -> str:
    lines = content.split('\n')
    cleaned = []
    prev_line = ""
    seen_headings = set()

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip "Chapter N Title" lines (header/footer artifacts)
        if re.match(r'^Chapter \d+', line) and not line.startswith('#'):
            i += 1
            continue

        # Skip standalone page numbers
        if re.match(r'^\d+$', line.strip()):
            i += 1
            continue

        # Skip horizontal rules
        if re.match(r'^---+$', line.strip()):
            i += 1
            continue

        # Skip duplicate section headers (e.g., "## 3.1. Title" appearing as page header)
        # These typically appear without a blank line before them and duplicate a real heading
        if re.match(r'^##\s+\d+\.\d+\.?\s+\w', line):
            # Check if this exact text (minus the ##) was recently seen
            heading_text = re.sub(r'^##\s+', '', line).strip()
            heading_key = re.sub(r'[.\s]+', '', heading_text.lower())
            if heading_key in seen_headings:
                i += 1
                continue
            seen_headings.add(heading_key)

        # Track headings we've seen
        if line.startswith('#'):
            heading_text = re.sub(r'^#+\s+', '', line).strip()
            heading_key = re.sub(r'[.\s]+', '', heading_text.lower())
            seen_headings.add(heading_key)

        cleaned.append(line)
        prev_line = line
        i += 1

    content = '\n'.join(cleaned)

    # Convert HTML entities
    content = content.replace('&gt;', '>')
    content = content.replace('&lt;', '<')
    content = content.replace('&amp;', '&')
    content = content.replace('&nbsp;', ' ')
    content = content.replace('&#39;', "'")
    content = content.replace('&quot;', '"')

    # Normalize heading hierarchy:
    # Main chapter title: # (keep as is if present)
    # Sections (X.Y): ##
    # Subsections (X.Y.Z): ###
    # Sub-subsections (X.Y.Z.W): ####

    def normalize_heading(match):
        hashes = match.group(1)
        num = match.group(2)
        title = match.group(3)

        # Count dots to determine level
        dots = num.count('.')
        if dots == 0:
            # Chapter level (e.g., "2"): use ##
            return f"## {num} {title}"
        elif dots == 1:
            # Section level (e.g., "2.1"): use ##
            return f"## {num} {title}"
        elif dots == 2:
            # Subsection level (e.g., "2.1.1"): use ###
            return f"### {num} {title}"
        else:
            # Deeper: use ####
            return f"#### {num} {title}"

    # Match headings with numbers like "# 2.1 Title" or "## 2.1.1 Title"
    content = re.sub(
        r'^(#{1,4})\s+(\d+(?:\.\d+)*)\s+(.+)$',
        normalize_heading,
        content,
        flags=re.MULTILINE
    )

    # Remove trailing period from section numbers in headings
    content = re.sub(r'^(#{2,4}\s+\d+(?:\.\d+)*)\.\s+', r'\1 ', content, flags=re.MULTILINE)

    # Fix LaTeX display blocks: remove blank lines between $$ and content
    # Pattern: $$ followed by blank lines, then content, then blank lines, then $$
    def collapse_display_math(match):
        content_inner = match.group(1).strip()
        return f'$$\n{content_inner}\n$$'

    content = re.sub(r'\$\$\s*\n\s*(.*?)\s*\n\s*\$\$', collapse_display_math, content, flags=re.DOTALL)

    # Clean up multiple blank lines (more than 2 consecutive)
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    # Remove blank lines at start of file
    content = content.lstrip('\n')

    # Ensure single newline at end
    content = content.rstrip('\n') + '\n'

    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run scripts/cleanup_ocr.py <file.md> [--inplace]")
        print("       uv run scripts/cleanup_ocr.py <directory> [--inplace]")
        sys.exit(1)

    path = Path(sys.argv[1])
    inplace = '--inplace' in sys.argv

    if path.is_dir():
        files = list(path.glob('*.md'))
    else:
        files = [path]

    for f in files:
        content = f.read_text(encoding='utf-8')
        cleaned = clean_markdown(content)

        if inplace:
            f.write_text(cleaned, encoding='utf-8')
            print(f"Cleaned: {f.name}")
        else:
            print(f"=== {f.name} ===")
            print(cleaned[:2000])
            print("...")


if __name__ == '__main__':
    main()
