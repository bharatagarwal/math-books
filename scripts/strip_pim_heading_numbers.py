# /// script
# requires-python = ">=3.10"
# ///
"""Strip redundant chapter/section numbers from PIM (Jeremy Kun) headings, in
place, and rewrite prose "Section N.M" cross-references to the section title so
they don't dangle.

Rules (headings, outside code fences only):
  - "# Chapter N Title" / "# Chapter N: Title"  -> "# Title"
  - "## N.M[.K] Title" / "## N.M. Title"        -> "## Title"   (any depth)
  - bare-number headings ("### 2.2.")           -> KEPT (the number is the
    content: these are exercise headings)
  - semantic labels ("Theorem 2.4.", "Definition 8.6.", "Proof.",
    "Proposition 8.5.", "Lemma ...", "Corollary ...")  -> KEPT (cited in prose)

Prose: "Section N.M" / "section N.M" -> 'the "<Title>" section'.

Chapter-level numbers in prose ("Chapter 16") are intentionally KEPT: the reader
sidebar still shows chapter numbers, so those references stay navigable.
"""
import glob
import re
import sys

PIM = sorted(glob.glob("markdown/pim/*.md"))

H_CHAPTER = re.compile(r'^(#{1,6})\s+Chapter\s+\d+\s*:?\s+(.*\S)\s*$')
# "N.M" or "N.M.K" (>=2 components) followed by a real title
H_SECTION = re.compile(r'^(#{1,6})\s+\d+(?:\.\d+)+\.?\s+(\S.*\S|\S)\s*$')
# heading that is ONLY a number (exercise heading) -> keep
H_BARE = re.compile(r'^#{1,6}\s+\d+(?:\.\d+)*\.?\s*$')
# semantic labelled headings -> keep
H_LABEL = re.compile(
    r'^#{1,6}\s+(Theorem|Lemma|Proposition|Corollary|Definition|Proof|'
    r'Example|Remark|Claim|Exercise|Problem)\b', re.I)


def build_section_title_map(files):
    """Map 'N.M[.K]' -> title, from every numbered section heading in PIM."""
    m = {}
    sec = re.compile(r'^#{1,6}\s+(\d+(?:\.\d+)+)\.?\s+(\S.*\S|\S)\s*$')
    for f in files:
        infence = False
        for line in open(f, encoding="utf-8"):
            s = line.rstrip("\n")
            if s.lstrip().startswith("```"):
                infence = not infence
                continue
            if infence:
                continue
            mm = sec.match(s)
            if mm:
                m[mm.group(1)] = mm.group(2).strip()
    return m


def transform(path, secmap):
    out = []
    infence = False
    changed = 0
    refs_rewritten = 0
    for line in open(path, encoding="utf-8"):
        s = line.rstrip("\n")
        if s.lstrip().startswith("```"):
            infence = not infence
            out.append(s)
            continue
        if infence:
            out.append(s)
            continue

        new = s
        if s.lstrip().startswith("#"):
            if H_LABEL.match(s) or H_BARE.match(s):
                pass  # keep as-is
            else:
                cm = H_CHAPTER.match(s)
                sm = H_SECTION.match(s)
                if cm:
                    new = cm.group(1) + " " + cm.group(2)
                elif sm:
                    new = sm.group(1) + " " + sm.group(2)
            if new != s:
                changed += 1
        else:
            # rewrite prose "Section N.M" cross-refs to the section title
            def repl(mo):
                nonlocal refs_rewritten
                num = mo.group(2)
                title = secmap.get(num)
                if not title:
                    return mo.group(0)  # unknown -> leave untouched
                refs_rewritten += 1
                return 'the "%s" section' % title
            new = re.sub(r'\b([Ss]ection)\s+(\d+(?:\.\d+)+)',
                         repl, new)

        out.append(new)

    text = "\n".join(out)
    if not text.endswith("\n"):
        text += "\n"
    open(path, "w", encoding="utf-8").write(text)
    return changed, refs_rewritten


def main():
    secmap = build_section_title_map(PIM)
    dry = "--apply" not in sys.argv
    total_h = total_r = 0
    for f in PIM:
        if dry:
            # report only
            import io
            buf = open(f, encoding="utf-8").read()
            # quick count using the same regexes
            infence = False
            ch = rf = 0
            for line in buf.split("\n"):
                if line.lstrip().startswith("```"):
                    infence = not infence
                    continue
                if infence:
                    continue
                if line.lstrip().startswith("#") and not (
                        H_LABEL.match(line) or H_BARE.match(line)):
                    if H_CHAPTER.match(line) or H_SECTION.match(line):
                        ch += 1
                else:
                    rf += len(re.findall(r'\b[Ss]ection\s+\d+(?:\.\d+)+', line))
            if ch or rf:
                print(f"  {f.split('/')[-1]}: {ch} headings, {rf} refs")
            total_h += ch
            total_r += rf
        else:
            ch, rf = transform(f, secmap)
            if ch or rf:
                print(f"  {f.split('/')[-1]}: {ch} headings, {rf} refs")
            total_h += ch
            total_r += rf
    mode = "WOULD strip" if dry else "stripped"
    print(f"\n{mode} {total_h} heading numbers, "
          f"rewrote {total_r} section cross-refs.")
    if dry:
        print("(dry run — re-run with --apply to write)")


if __name__ == "__main__":
    main()
