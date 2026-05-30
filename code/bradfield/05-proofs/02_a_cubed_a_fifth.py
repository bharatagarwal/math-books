# uv run --with sympy --with z3-solver python \
#   code/bradfield/05-proofs/02_a_cubed_a_fifth.py
# Post-class problem: show that if a^3 > a then a^5 > a (for real a).
import sympy as sp
from z3 import Real, ForAll, Implies, Solver, Not, unsat

a = sp.Symbol("a", real=True)

# The whole proof is one algebraic identity: a^5 - a factors THROUGH a^3 - a.
#   a^5 - a = (a^3 - a)(a^2 + 1)
identity = sp.expand((a**3 - a) * (a**2 + 1)) - (a**5 - a)
assert sp.simplify(identity) == 0

# Since a^2 + 1 > 0 for every real a, the sign of (a^5 - a) equals the sign of
# (a^3 - a). So a^3 - a > 0  implies  a^5 - a > 0, i.e. a^5 > a. QED.

# Now let z3 check the implication over the reals with NO hints -- a machine-
# checked proof that the statement holds for ALL real a (negation unsat).
z = Real("a")
claim = ForAll([z], Implies(z**3 > z, z**5 > z))
s = Solver()
s.add(Not(claim))
assert s.check() == unsat

print("identity a^5 - a = (a^3 - a)(a^2 + 1):", sp.factor(a**5 - a))
print("z3 confirms: for all real a, a^3 > a  =>  a^5 > a")
