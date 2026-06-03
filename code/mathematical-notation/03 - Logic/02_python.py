# uv run --with z3-solver python
# Quantifiers in Z3: ∀ and ∃ become ForAll and Exists.
# ∀x ∈ R, x² ≥ 0  — can Z3 find a counterexample?
from z3 import Real, ForAll, Exists, Solver, sat

x = Real('x')
y = Real('y')

# "For all x, x² ≥ 0" — try to REFUTE it
s = Solver()
s.add(x * x < 0)  # negation: find x where x² < 0
print(f"∀x, x² ≥ 0 refuted? {s.check()}")
# unsat → no counterexample → the universal claim holds

# "∃y ∈ R, x + y = 0" — find such y for x = 7
s2 = Solver()
s2.add(7 + y == 0)
print(f"∃y, 7 + y = 0? {s2.check()}, y = {s2.model()[y]}")

# The FALSE claim: "∃y ∈ R, ∀x ∈ R, x + y = 0"
# (one magic y that zeroes every x)
s3 = Solver()
s3.add(ForAll([x], x + y == 0))
print(f"∃y ∀x, x+y=0? {s3.check()}")
# unsat → no such magic y exists
