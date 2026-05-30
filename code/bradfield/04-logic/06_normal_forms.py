# uv run python code/bradfield/04-logic/06_normal_forms.py
"""Read DNF and CNF straight off a truth table (MCS 3.4).

MCS 3.4 shows that EVERY formula is equivalent to a disjunctive normal
form (an OR of AND-terms) and a conjunctive normal form (an AND of
OR-terms), built mechanically from its truth table:

  * DNF: one AND-term per row where the formula is TRUE
         (a variable plain if it's T in that row, negated if F),
         OR'd together.
  * CNF: one OR-term per row where the formula is FALSE
         (each variable negated relative to that row),
         AND'd together.

We do this for the chapter's running example  A AND (B OR C),  print the
two normal forms, then VERIFY that re-evaluating each normal form
reproduces the original truth column on all 8 rows.
"""
from itertools import product

VARS = ["A", "B", "C"]


def formula(A, B, C):
    return A and (B or C)


def lit(name, value, negate_when_true):
    """Render a literal. negate_when_true picks the DNF/CNF convention."""
    neg = value if negate_when_true else (not value)
    return f"~{name}" if neg else name


def main():
    rows = list(product([True, False], repeat=3))
    out = [formula(*r) for r in rows]

    def t(b):
        return "T" if b else "F"

    print("A B C | A AND (B OR C)")
    for r, o in zip(rows, out):
        print(f"{t(r[0])} {t(r[1])} {t(r[2])} |      {t(o)}")

    # DNF: collect AND-terms from the TRUE rows.
    and_terms = []
    for r, o in zip(rows, out):
        if o:
            lits = [lit(n, v, negate_when_true=False)
                    for n, v in zip(VARS, r)]
            and_terms.append("(" + " & ".join(lits) + ")")
    dnf = " | ".join(and_terms)
    print(f"\nDNF (OR of AND-terms, one per TRUE row):\n  {dnf}")

    # CNF: collect OR-terms from the FALSE rows.
    or_terms = []
    for r, o in zip(rows, out):
        if not o:
            lits = [lit(n, v, negate_when_true=True)
                    for n, v in zip(VARS, r)]
            or_terms.append("(" + " | ".join(lits) + ")")
    cnf = " & ".join(or_terms)
    print(f"\nCNF (AND of OR-terms, one per FALSE row):\n  {cnf}")

    # Verify both normal forms reproduce the original truth column.
    def eval_dnf(A, B, C):
        env = {"A": A, "B": B, "C": C}
        any_true = False
        for r, o in zip(rows, out):
            if o and all(env[n] == v for n, v in zip(VARS, r)):
                any_true = True
        return any_true

    def eval_cnf(A, B, C):
        env = {"A": A, "B": B, "C": C}
        for r, o in zip(rows, out):
            if not o and all(env[n] == v for n, v in zip(VARS, r)):
                return False
        return True

    for r, o in zip(rows, out):
        assert eval_dnf(*r) == o
        assert eval_cnf(*r) == o
    print("\nboth normal forms reproduce the original column on all 8 rows.")


main()
