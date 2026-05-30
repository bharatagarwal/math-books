# uv run --with z3-solver python
from z3 import BitVec, Solver, sat, UGT, ULT

n = BitVec('n', 32)
divisor = BitVec('divisor', 32)
quadratic = n*n + n + 41

solver = Solver()
solver.add(n >= 0)
solver.add(UGT(divisor, 1))
solver.add(ULT(divisor, quadratic))
solver.add(quadratic % divisor == 0)

if solver.check() == sat:
    model = solver.model()
    n_found = model[n].as_long()
    d_found = model[divisor].as_long()
    result = n_found**2 + n_found + 41
    print(f"n={n_found}: {n_found}² + {n_found} + 41 = {result} = {d_found} × {result // d_found}")
# Output: n=1439208670 (Z3 picks an arbitrary counterexample, not the smallest)
