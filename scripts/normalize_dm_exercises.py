# /// script
# requires-python = ">=3.10"
# ///
"""Normalize Lovász (dm) exercises into a consistent blockquote form.

Every exercise becomes a blockquote whose first token is the bolded
exercise number:  `> **2.5** Name sets having cardinality ...`

Rules (see task spec):
- An exercise starts with `N.M ` at the start of a line (optionally already
  inside a blockquote `> `, optionally already bolded `**N.M**`).
- Multi-part / multi-line exercises (following `(a)`/`(b)` paragraphs or a
  trailing `$$...$$` display that belongs to the exercise) are grouped into
  ONE blockquote, every line prefixed with `> `.
- A run of consecutive different exercises -> separate adjacent blockquotes.
- Non-exercise blockquotes (no leading number) are preserved as-is.
- NEVER touch: `## ` headings, code fences, `<!-- ... -->` directives/markers.
- Preserve all text/math verbatim; only restructure.

Usage: python normalize_dm_exercises.py [--write] file1.md [file2.md ...]
"""
import re
import sys

# Exercise-number at start of (de-quoted) line:  "2.5 ", "10.1 ", "**3.2**" ...
EX_RE = re.compile(r'^\s*(?:\*\*)?(\d+\.\d+)(?:\*\*)?[.)]?\s+(.*)$', re.DOTALL)
# A part marker like "(a) ", "(b) ", "(iv) " starting a paragraph.
PART_RE = re.compile(r'^\s*\([a-z0-9ivx]+\)\s', re.IGNORECASE)
# A pure display-math paragraph (single line $$...$$ or $...$ only).
DISPLAY_RE = re.compile(r'^\s*\${1,2}.*\${1,2}\s*$')


def is_exercise_start(deq):
    """deq = line with any leading '> ' removed. Return (num, rest) or None."""
    m = EX_RE.match(deq)
    if not m:
        return None
    return m.group(1), deq  # keep full de-quoted line text


def dequote(line):
    """Strip a single leading blockquote marker. Return (was_quoted, text)."""
    if line.startswith('> '):
        return True, line[2:]
    if line == '>':
        return True, ''
    if line.startswith('>'):
        return True, line[1:]
    return False, line


def emit_exercise(num, body_lines):
    """body_lines: list of de-quoted text lines for ONE exercise.
    Returns blockquote lines with the leading number bolded."""
    # Bold the leading number on the first content line.
    first = body_lines[0]
    m = EX_RE.match(first)
    rest = m.group(2) if m else first
    # Reconstruct first line as "**NUM** rest" (rest may be empty).
    first_new = f'**{num}** {rest}'.rstrip()
    out = [first_new] + body_lines[1:]
    # Trim trailing blank lines inside the exercise.
    while out and out[-1].strip() == '':
        out.pop()
    return ['> ' + l if l.strip() != '' else '>' for l in out]


def emit_plain_blockquote(body_lines):
    """A non-exercise blockquote segment, preserved verbatim as a blockquote."""
    out = list(body_lines)
    while out and out[-1].strip() == '':
        out.pop()
    return ['> ' + l if l.strip() != '' else '>' for l in out]


def process_blockquote_region(deq_lines):
    """deq_lines: de-quoted lines of a maximal `>`-region (blank '>' -> '').
    Re-segment into per-exercise blockquotes + preserved non-exercise ones."""
    # Split into paragraphs separated by blank lines, keeping order.
    segments = []  # list of (kind, [lines]) where kind in {'ex','plain'}
    cur_kind = None
    cur = []
    cur_num = None

    def flush():
        nonlocal cur, cur_kind, cur_num
        if cur:
            segments.append((cur_kind, cur_num, cur))
        cur, cur_kind, cur_num = [], None, None

    i = 0
    n = len(deq_lines)
    while i < n:
        line = deq_lines[i]
        ex = is_exercise_start(line)
        if ex:
            # New exercise begins: close any current segment.
            flush()
            cur_kind = 'ex'
            cur_num = ex[0]
            cur = [line]
            i += 1
            # Absorb continuation lines until the next exercise start.
            while i < n:
                nxt = deq_lines[i]
                if is_exercise_start(nxt):
                    break
                cur.append(nxt)
                i += 1
            flush()
        else:
            # Non-exercise content before/after exercises -> plain bq segment.
            if cur_kind not in (None, 'plain'):
                flush()
            cur_kind = 'plain'
            cur.append(line)
            i += 1
    flush()

    out = []
    for idx, (kind, num, lines) in enumerate(segments):
        if idx > 0:
            out.append('')  # blank line separates adjacent blockquotes
        if kind == 'ex':
            out.extend(emit_exercise(num, lines))
        else:
            out.extend(emit_plain_blockquote(lines))
    return out


def process(text):
    lines = text.split('\n')
    out = []
    i = 0
    n = len(lines)
    in_fence = False
    while i < n:
        line = lines[i]
        stripped = line.lstrip()

        # Code fences: pass through untouched.
        if stripped.startswith('```'):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if in_fence:
            out.append(line)
            i += 1
            continue

        # Blockquote region: gather maximal run of '>'-lines.
        if line.startswith('>'):
            region = []
            while i < n and lines[i].startswith('>'):
                _, txt = dequote(lines[i])
                region.append(txt)
                i += 1
            out.extend(process_blockquote_region(region))
            continue

        # Plain exercise start (not a heading, not a comment).
        if not stripped.startswith('## ') and not stripped.startswith('#'):
            ex = is_exercise_start(line)
            if ex and not stripped.startswith('<!--'):
                num = ex[0]
                body = [line]
                i += 1
                # Gather continuation paragraphs: part-markers or pure display
                # math, separated by single blank lines. Stop at the first
                # ordinary prose paragraph, heading, blank-run end, or next ex.
                while i < n:
                    # Expect a blank separator then a candidate paragraph.
                    if lines[i].strip() != '':
                        # No blank separator -> continuation on adjacent line
                        # only if it's a part/display; otherwise stop.
                        cand = lines[i]
                        if (PART_RE.match(cand) or DISPLAY_RE.match(cand)) \
                                and not is_exercise_start(cand):
                            body.append(cand)
                            i += 1
                            continue
                        break
                    # lines[i] is blank: peek the next non-blank paragraph.
                    j = i
                    while j < n and lines[j].strip() == '':
                        j += 1
                    if j >= n:
                        break
                    cand = lines[j]
                    cstr = cand.lstrip()
                    if cstr.startswith('#') or cstr.startswith('>') \
                            or cstr.startswith('```') or cstr.startswith('<!--') \
                            or cstr.startswith('!['):
                        break
                    if is_exercise_start(cand):
                        break
                    if PART_RE.match(cand) or DISPLAY_RE.match(cand):
                        # Pull in the blank lines + this paragraph (which may
                        # itself span multiple lines until the next blank).
                        body.append('')
                        k = j
                        while k < n and lines[k].strip() != '':
                            body.append(lines[k])
                            k += 1
                        i = k
                        continue
                    break
                out.extend(emit_exercise(num, body))
                continue

        out.append(line)
        i += 1

    return '\n'.join(out)


def main():
    args = sys.argv[1:]
    write = False
    if '--write' in args:
        write = True
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
