# /// script
# requires-python = ">=3.10"
# ///
"""Normalize MCS (mcs/01 - Proofs) `Problem N.M.` markers to a consistent form.

These problems are multi-paragraph (with their own sub-headings, display math
and lists), so they are NOT wrapped in blockquotes (that would be destructive
and would swallow following structure). Instead each problem *marker* is
normalized to a consistent `### Problem N.M.` heading so the reader outline and
the `styleExercises` badge pass treat them uniformly. Bare markers and markers
with inline body text are fixed up; real section headings ("Problems for
Section ...", "Class Problems", etc.) are left untouched.

Usage: python normalize_mcs_problems.py [--write] file1.md [...]
"""
import re
import sys

# A problem marker: optional leading #'s, then "Problem N.M." then optional
# inline body on the same line. Must be the WHOLE label (Problem <num>.) — not
# "Problems for Section".
MARKER_RE = re.compile(
    r'^\s*#{0,6}\s*Problem\s+(\d+\.\d+)\.?\s*(.*)$'
)


def process(text):
    lines = text.split('\n')
    out = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        m = MARKER_RE.match(line)
        # Guard: don't match "Problems ..." section headings (MARKER_RE already
        # requires "Problem <digits>", so "Problems for Section" won't match).
        if m:
            num = m.group(1)
            inline_body = m.group(2).strip()
            out.append(f'### Problem {num}.')
            if inline_body:
                out.append('')
                out.append(inline_body)
            continue
        out.append(line)
    return '\n'.join(out)


def main():
    args = sys.argv[1:]
    write = '--write' in args
    if write:
        args.remove('--write')
    for path in args:
        with open(path, encoding='utf-8') as f:
            text = f.read()
        new = process(text)
        if write:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new)
            print(f'wrote {path}')
        else:
            sys.stdout.write(new)


if __name__ == '__main__':
    main()
