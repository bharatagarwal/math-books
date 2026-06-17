# uv run --with sympy python
# SymPy's pretty-printer renders Greek names as Unicode glyphs.
# In scripts, use pprint(); in the REPL, call init_printing() once.
from sympy import Symbol, pprint

# Greek letter names pretty-print as their Unicode glyphs
alpha = Symbol('alpha')
theta = Symbol('theta')
pprint(alpha)            # α
pprint(theta)            # θ
pprint(alpha + theta)    # α + θ

# Underscore creates a subscript — mirrors x_i in math notation
alpha_i = Symbol('alpha_i')
pprint(alpha_i)          # αᵢ

# Assumptions let SymPy reason about a symbol's properties
x = Symbol('x', positive=True)
print(x.is_positive)     # True
print(x.is_negative)     # False
