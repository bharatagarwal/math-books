# uv run --with sympy python
# Descartes' convention: a,b,c for knowns; x,y,z for unknowns.
# SymPy follows this — symbols are unknowns by default.
from sympy import symbols, solve, Eq

a, b, c = 2, -3, 1          # known coefficients
x = symbols('x')             # unknown
solutions = solve(a*x**2 + b*x + c, x)
print(f"{a}x² + ({b})x + {c} = 0")
print(f"solutions: x = {solutions}")
# 2x² + (-3)x + 1 = 0
# solutions: x = [1/2, 1]
