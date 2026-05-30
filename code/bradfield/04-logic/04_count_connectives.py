# uv run python code/bradfield/04-logic/04_count_connectives.py
"""Discover that there are exactly 16 binary connectives (MCS ch 3).

A binary connective is any function from the four input rows
(TT, TF, FT, FF) to a single output bit. So a connective IS just its
output column: four bits, hence 2^4 = 16 possible connectives. Instead
of taking that on faith, we build all of them and watch the named ones
(AND, OR, XOR, IMPLIES, IFF, ...) fall out of the enumeration.
"""
from itertools import product

ROWS = list(product([True, False], repeat=2))  # TT, TF, FT, FF


def column(fn):
    """The 4-bit output column that defines a connective."""
    return tuple(fn(p, q) for p, q in ROWS)


# The connectives MCS names, keyed by their output column.
NAMED = {
    column(lambda p, q: p and q): "AND",
    column(lambda p, q: p or q): "OR",
    column(lambda p, q: p != q): "XOR",
    column(lambda p, q: (not p) or q): "IMPLIES",
    column(lambda p, q: p == q): "IFF",
    column(lambda p, q: not (p and q)): "NAND",
    column(lambda p, q: not (p or q)): "NOR",
    column(lambda p, q: True): "TRUE (tautology)",
    column(lambda p, q: False): "FALSE (contradiction)",
}


def t(b):
    return "T" if b else "F"


def main():
    # Every 4-bit column is a connective: enumerate all 2^4 of them.
    cols = list(product([True, False], repeat=4))
    print(f"input rows: {[t(p) + t(q) for p, q in ROWS]}")
    print(f"total binary connectives = 2^4 = {len(cols)}\n")
    named = 0
    for col in cols:
        label = NAMED.get(col, "")
        if label:
            named += 1
        bits = " ".join(t(b) for b in col)
        print(f"  {bits}   {label}")
    assert len(cols) == 16
    assert named == len(NAMED)
    print(f"\n{named} of the 16 have everyday names; the rest are "
          f"nameless but just as real.")


main()
