# uv run --with z3-solver python
from z3 import *

n = Int('n')
d = Int('d')
expr = n*n + n + 41

solver = Solver()
solver.add(n >= 0)
solver.add(d > 1, d < expr)  # d is a proper divisor
solver.add(expr % d == 0)    # d divides the expression

if solver.check() == sat:
    m = solver.model()
    n_val = m[n].as_long()
    d_val = m[d].as_long()
    result = n_val**2 + n_val + 41
    print(f"n={n_val}: {n_val}² + {n_val} + 41 = {result} = {d_val} × {result // d_val}")
# Output: n=40: 40² + 40 + 41 = 1681 = 41 × 41
