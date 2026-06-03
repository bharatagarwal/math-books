# /// script
# requires-python = ">=3.10"
# ///
"""Split over-long Markdown prose paragraphs at sentence boundaries.

Rubric
------
* Operate ONLY on prose paragraphs (blank-line-separated running text). Never
  touch headings, lists, blockquotes, tables, fenced code, display-math
  ($$ ... $$), figures, HTML comments / include / carousel directives, or HRs.
* The only edit is inserting a paragraph break (blank line) at a sentence
  boundary. No word, symbol, or piece of math is ever added, removed, or
  reordered. The transform is provably whitespace-only (self-checked per file).
* Boundaries are detected outside protected spans ($...$, $$...$$, `code`) and
  skip common abbreviations / initials / decimals.
* A long paragraph is partitioned into the FEWEST contiguous pieces that each
  fit the budget, and among those, the partition that MAXIMISES the shortest
  piece -- i.e. the anti-widow objective. If the only way to reach the budget
  would orphan a fragment shorter than --widow-min, the paragraph is kept whole
  (a little over budget) and flagged, because "no widows" wins the tie.

Usage:
  uv run scripts/pim_para_split.py [PATHS...] [--apply] [--limit N]
                                   [--widow-min N] [--quiet]
  (dry-run by default; --apply writes the files.)
"""
from __future__ import annotations

import re
import sys
import pathlib

# ---- block classification (shared semantics with pim_para_lint.py) ----------
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


def is_nonprose(first: str) -> bool:
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


# ---- sentence tokenisation --------------------------------------------------
ABBREV = {
    "e.g", "i.e", "etc", "cf", "vs", "al", "et", "viz", "ibid", "resp",
    "approx", "fig", "figs", "eq", "eqs", "thm", "def", "prop", "lem", "cor",
    "ch", "chap", "sec", "vol", "vols", "no", "nos", "pp", "pg", "ed", "eds",
    "dr", "mr", "mrs", "ms", "prof", "gen", "st", "jr", "sr", "inc", "co",
    "ltd", "corp", "dept", "univ", "ph", "trans", "col", "art", "ref",
}

# protected spans: $$...$$, $...$, `...`, and quotations (no break inside a
# quote — a multi-sentence quotation must stay in one paragraph). Both straight
# ("...") and smart (“...”) double quotes; single quotes are left alone so
# apostrophes (don't, we'll) aren't mistaken for quote delimiters.
_PROT = re.compile(
    r"\$\$.*?\$\$|\$[^$]*\$|`[^`]*`|\"[^\"]*\"|“[^”]*”",
    re.DOTALL,
)


def _protected_mask(text: str) -> list[bool]:
    mask = [False] * len(text)
    for m in _PROT.finditer(text):
        for k in range(m.start(), m.end()):
            mask[k] = True
    return mask


# end punct, optional closing quotes/brackets, optional footnote ref, then ws
_BOUND = re.compile(r"[.?!][\"')\]]*(?:\[\^[^\]]+\])?[\"')\]]*(\s+)")
_OPENER = re.compile(r"[A-Z0-9$\\(\[\"'*_]")
_TRAIL_TOKEN = re.compile(r"([A-Za-z][A-Za-z.]*)$")


def sentence_spans(text: str) -> list[tuple[int, int, int]]:
    """Return [(start, end, ws_end)]: sentence chars [start,end), trailing
    whitespace ending at ws_end. Last sentence has ws_end == end."""
    mask = _protected_mask(text)
    cuts: list[tuple[int, int]] = []  # (ws_start, ws_end)
    for m in _BOUND.finditer(text):
        punct = m.start()           # index of . ? !
        ws_start = m.start(1)
        ws_end = m.end(1)
        if mask[punct] or mask[ws_start]:
            continue
        if ws_end >= len(text):
            continue
        nxt = text[ws_end]
        if not _OPENER.match(nxt):
            continue
        # abbreviation / initial guard on the token before the punctuation
        head = text[:punct]
        tm = _TRAIL_TOKEN.search(head)
        if tm:
            tok = tm.group(1).rstrip(".")
            letters = tok.replace(".", "")
            if tok.lower() in ABBREV or len(letters) <= 1:
                continue
        cuts.append((ws_start, ws_end))

    spans: list[tuple[int, int, int]] = []
    prev = 0
    for ws_start, ws_end in cuts:
        spans.append((prev, ws_start, ws_end))
        prev = ws_end
    spans.append((prev, len(text), len(text)))
    return spans


# ---- partitioning -----------------------------------------------------------
NEG = float("-inf")


def best_partition(starts, ends, limit):
    """Partition sentences (given start/end offsets) into the fewest pieces with
    each piece length <= limit, maximising the shortest piece. Returns
    (cut_sentence_indices, min_piece_len) or (None, None) if infeasible at any k
    up to one-piece-per-sentence."""
    m = len(starts)

    def piece_len(i, j):  # sentences i..j inclusive
        return ends[j] - starts[i]

    for k in range(2, m + 1):
        # dp[j][p] = best achievable min-piece using first j sentences in p pieces
        dp = [[NEG] * (k + 1) for _ in range(m + 1)]
        par = [[-1] * (k + 1) for _ in range(m + 1)]
        dp[0][0] = float("inf")
        for j in range(1, m + 1):
            pmax = min(k, j)
            for p in range(1, pmax + 1):
                best = NEG
                bt = -1
                for t in range(p - 1, j):  # last piece = sentences t..j-1
                    ln = piece_len(t, j - 1)
                    if ln > limit:
                        continue
                    if dp[t][p - 1] == NEG:
                        continue
                    val = min(dp[t][p - 1], ln)
                    if val > best:
                        best = val
                        bt = t
                dp[j][p] = best
                par[j][p] = bt
        if dp[m][k] != NEG:
            # reconstruct cut sentence indices (start sentence of each piece >0)
            cuts = []
            j, p = m, k
            while p > 0:
                t = par[j][p]
                if t > 0:
                    cuts.append(t)
                j, p = t, p - 1
            cuts.sort()
            return cuts, dp[m][k]
    return None, None


def split_paragraph(text, limit, widow_min):
    """Return (new_text, flag). flag in {None,'kept-widow','split-widow',
    'sentence-over'}."""
    spans = sentence_spans(text)
    if len(spans) == 1:
        return text, "sentence-over"  # single sentence over budget; can't split
    starts = [s[0] for s in spans]
    ends = [s[1] for s in spans]
    cuts, min_piece = best_partition(starts, ends, limit)
    flag = None
    if cuts is None:
        # some single sentence exceeds the budget: cut at every boundary anyway
        cuts = list(range(1, len(spans)))
        flag = "sentence-over"
    elif min_piece < widow_min:
        if len(text) <= limit + widow_min:
            return text, "kept-widow"  # orphan unavoidable & overflow small: keep whole
        flag = "split-widow"

    # apply cuts right-to-left: replace inter-sentence whitespace with "\n\n"
    out = text
    for t in sorted(cuts, reverse=True):
        ws_start = spans[t - 1][1]
        ws_end = spans[t - 1][2]
        out = out[:ws_start] + "\n\n" + out[ws_end:]
    return out, flag


# ---- file processing --------------------------------------------------------
def process_file(path, limit, widow_min):
    raw = path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    n = len(lines)
    out: list[str] = []
    block: list[str] = []
    stats = {"split": 0, "new_paras": 0, "flags": {}}

    def flush():
        if not block:
            return
        text = "\n".join(block)
        if is_nonprose(block[0]) or len(text) <= limit:
            out.extend(block)
            return
        new_text, flag = split_paragraph(text, limit, widow_min)
        if flag:
            stats["flags"].setdefault(flag, 0)
            stats["flags"][flag] += 1
        if new_text != text:
            stats["split"] += 1
            stats["new_paras"] += new_text.count("\n\n")
        out.extend(new_text.split("\n"))

    i = 0
    while i < n:
        line = lines[i]
        ls = line.lstrip()
        if FENCE.match(line):
            flush(); block = []
            marker = "```" if ls.startswith("```") else "~~~"
            out.append(line)
            i += 1
            while i < n and not lines[i].lstrip().startswith(marker):
                out.append(lines[i]); i += 1
            if i < n:
                out.append(lines[i]); i += 1
            continue
        if line.strip() == "$$":
            flush(); block = []
            out.append(line); i += 1
            while i < n and lines[i].strip() != "$$":
                out.append(lines[i]); i += 1
            if i < n:
                out.append(lines[i]); i += 1
            continue
        if line.strip() == "":
            flush(); block = []
            out.append(line); i += 1
            continue
        block.append(line); i += 1
    flush()

    new_raw = "\n".join(out)
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    ok = norm(new_raw) == norm(raw)
    return new_raw, stats, ok


def iter_md(paths):
    files = []
    for p in paths:
        pp = pathlib.Path(p)
        if pp.is_dir():
            files.extend(sorted(pp.rglob("*.md")))
        elif pp.suffix == ".md":
            files.append(pp)
    return files


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    quiet = "--quiet" in args
    limit, widow_min = 500, 120
    for opt, default in (("--limit", None), ("--widow-min", None)):
        if opt in args:
            idx = args.index(opt)
            val = int(args[idx + 1])
            del args[idx: idx + 2]
            if opt == "--limit":
                limit = val
            else:
                widow_min = val
    paths = [a for a in args if not a.startswith("--")] or ["."]

    files = iter_md(paths)
    tot_split = 0
    tot_flags = {}
    bad = []
    for f in files:
        new_raw, stats, ok = process_file(f, limit, widow_min)
        if not ok:
            bad.append(f)
            print(f"!! {f}: CONTENT CHANGED beyond whitespace — NOT written")
            continue
        if stats["split"]:
            flagstr = ", ".join(f"{k}={v}" for k, v in stats["flags"].items())
            line = f"{f}: split {stats['split']} → +{stats['new_paras']} paras"
            if flagstr:
                line += f"  [{flagstr}]"
            if not quiet:
                print(line)
            tot_split += stats["split"]
            for k, v in stats["flags"].items():
                tot_flags[k] = tot_flags.get(k, 0) + v
        if apply and stats["split"]:
            f.write_text(new_raw, encoding="utf-8")

    print(f"\n{'=' * 60}")
    mode = "APPLIED" if apply else "dry-run"
    print(f"[{mode}] {tot_split} paragraph(s) split across {len(files)} file(s).")
    if tot_flags:
        print("flags: " + ", ".join(f"{k}={v}" for k, v in tot_flags.items()))
    if bad:
        print(f"ERRORS: {len(bad)} file(s) failed the whitespace-only self-check.")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
