# uv run --with sympy python
# SymPy's series() produces big-O terms automatically.
# sin(x) around x=0 is x - x³/6 + x⁵/120 - ... + O(x^n)
from sympy import symbols, sin, cos, exp, series

x = symbols('x')

# Taylor series of sin(x) around 0, up to x^7
s = series(sin(x), x, 0, 7)
print(f"sin(x) = {s}")
# sin(x) = x - x**3/6 + x**5/120 + O(x**7)

# The O() term is a real SymPy object you can inspect
print(f"O term:  {s.getO()}")
# O term:  O(x**7)

# Remove the O() to get the polynomial approximation
print(f"no O:    {s.removeO()}")
# no O:    x**5/120 - x**3/6 + x

# exp(x): shows e^x = 1 + x + x²/2 + O(x³)
print(f"\nexp(x) = {series(exp(x), x, 0, 3)}")
# exp(x) = 1 + x + x**2/2 + O(x**3)

# cos(x): even powers only
print(f"cos(x) = {series(cos(x), x, 0, 6)}")
# cos(x) = 1 - x**2/2 + x**4/24 + O(x**6)
