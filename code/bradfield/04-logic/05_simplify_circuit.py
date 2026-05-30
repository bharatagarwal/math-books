# uv run python code/bradfield/04-logic/05_simplify_circuit.py
"""Rebuild the MCS 3.2 circuit-simplification truth table by hand.

MCS turns the C/C++/Java condition
    x > 0 || (x <= 0 && y > 100)
into propositional logic by letting A be "x > 0" and B be "y > 100":
    A OR (NOT(A) AND B).
The chapter fills in the truth table one sub-column at a time and finds
the result column is identical to the column for the simpler A OR B --
so the two are EQUIVALENT and the code can be replaced by  x > 0 || y > 100.
We reproduce that column-by-column build and check the two final columns
match in every row (equivalence = same truth value everywhere).
"""
from itertools import product


def t(b):
    return "T" if b else "F"


def main():
    print("A B | NOT(A) | NOT(A) AND B | A OR (NOT(A) AND B) | A OR B")
    print("-" * 62)
    complicated, simple = [], []
    for A, B in product([True, False], repeat=2):
        nota = not A
        inner = nota and B          # NOT(A) AND B
        big = A or inner            # A OR (NOT(A) AND B)
        easy = A or B               # A OR B
        complicated.append(big)
        simple.append(easy)
        print(f"{t(A)} {t(B)} |   {t(nota)}    |      {t(inner)}       "
              f"|          {t(big)}          |   {t(easy)}")
    # Equivalence: the two result columns agree on every row.
    assert complicated == simple
    print("\nresult columns identical ->",
          "A OR (NOT(A) AND B)  ==  A OR B")
    print("so `x > 0 || (x <= 0 && y > 100)`")
    print("   simplifies to  `x > 0 || y > 100`")


main()
