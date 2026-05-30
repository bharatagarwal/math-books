# uv run --with z3-solver python code/bradfield/05-proofs/03_proof_by_cases.py
# Proof by cases (the r<s / r>s / r=s split), machine-checked over reals.
from z3 import Reals, ForAll, And, Or, If, Solver, Not, unsat, Abs

r, s = Reals("r s")

def valid(claim):
    sol = Solver(); sol.add(Not(claim))
    return sol.check() == unsat

# Claim: for all reals r, s:  max(r,s) + min(r,s) = r + s.
# A hand proof splits into cases r >= s and r < s; in each, max/min resolve and
# the two sides match. z3 checks all cases at once.
mx = If(r >= s, r, s)
mn = If(r >= s, s, r)
assert valid(ForAll([r, s], mx + mn == r + s))

# Claim: max(r,s) - min(r,s) = |r - s|. Same three-case structure.
assert valid(ForAll([r, s], mx - mn == Abs(r - s)))

# A cases proof can also be WRONG -- if the cases miss something, z3 finds it.
# Bogus claim: for all reals, r*s >= 0 ("a product is non-negative"). False when
# signs differ; the solver should NOT certify it.
assert not valid(ForAll([r, s], r * s >= 0))

print("max + min = r + s  : verified by cases (z3)")
print("max - min = |r - s|: verified by cases (z3)")
print("bogus 'r*s >= 0' correctly rejected")
