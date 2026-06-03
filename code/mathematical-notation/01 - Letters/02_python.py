# uv run --with sympy python
# Greek letters in math vs. their SymPy names.
# The notation maps directly to code.
from sympy import pi, E, oo, sqrt, Symbol

alpha = Symbol('alpha')
theta = Symbol('theta')

print(f"pi    = {pi}    ≈ {float(pi):.6f}")
print(f"e     = {E}     ≈ {float(E):.6f}")
print(f"sqrt2 = {sqrt(2)} ≈ {float(sqrt(2)):.6f}")
print(f"alpha and theta are symbolic: {alpha + theta}")
# pi    = pi    ≈ 3.141593
# e     = E     ≈ 2.718282
# sqrt2 = sqrt(2) ≈ 1.414214
# alpha and theta are symbolic: alpha + theta
