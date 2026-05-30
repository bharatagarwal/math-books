# uv run python code/bradfield/04-logic/01_truth_tables.py
# Connectives as functions on bits, and equivalence by exhaustive truth tables.
from itertools import product

NOT = lambda p: not p
AND = lambda p, q: p and q
OR = lambda p, q: p or q
IMPLIES = lambda p, q: (not p) or q          # p -> q is false only when p & ~q
IFF = lambda p, q: p == q

# Print the truth table for implication -- note the only False row is (T, F).
print("p q | p->q")
for p, q in product((False, True), repeat=2):
    print(int(p), int(q), " ", int(IMPLIES(p, q)))

def equivalent(f, g, n):
    # Two n-variable formulas are equivalent iff they agree on ALL 2^n rows.
    return all(f(*row) == g(*row) for row in product((False, True), repeat=n))

# Material implication: (p -> q) == (~p or q).
assert equivalent(IMPLIES, lambda p, q: OR(NOT(p), q), 2)

# Contrapositive: (p -> q) == (~q -> ~p).
assert equivalent(IMPLIES, lambda p, q: IMPLIES(NOT(q), NOT(p)), 2)

# De Morgan: ~(p and q) == (~p or ~q).
assert equivalent(lambda p, q: NOT(AND(p, q)),
                  lambda p, q: OR(NOT(p), NOT(q)), 2)

# A tautology is true on every row; a contradiction on none.
excluded_middle = lambda p: OR(p, NOT(p))
assert all(excluded_middle(p) for p in (False, True))

print("equivalences verified: material implication, contrapositive, De Morgan")
