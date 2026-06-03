# uv run --with sympy python
# SymPy: symbolic derivatives and integrals.
# Notation → code: d/dx → diff, ∫ → integrate, ∂/∂x → diff
from sympy import (
    symbols, diff, integrate, sin, cos, exp,
    oo, sqrt, pi, pprint, Function,
)

x, y, t = symbols('x y t')

# --- Single-variable derivatives ---
# d/dx [x³] = 3x²  (Leibniz: df/dx)
print("d/dx [x³] =", diff(x**3, x))
# 3*x**2

# Higher order: d²/dx² [x³] = 6x  (Newton: f'')
print("d²/dx² [x³] =", diff(x**3, x, 2))
# 6*x

# --- Indefinite integrals ---
# ∫ sin(x) dx = -cos(x) + C
print("∫ sin(x) dx =", integrate(sin(x), x))
# -cos(x)

# --- Definite integrals ---
# ∫₀^∞ e^{-x} dx = 1
print("∫₀^∞ e^{-x} dx =", integrate(exp(-x), (x, 0, oo)))
# 1

# The Gaussian integral: ∫_{-∞}^{∞} e^{-x²} dx = √π
print("∫ e^{-x²} dx =", integrate(exp(-x**2),
                                    (x, -oo, oo)))
# sqrt(pi)

# --- Partial derivatives ---
# ∂/∂x [x²y + y³] = 2xy
f = x**2 * y + y**3
print("∂f/∂x =", diff(f, x))   # 2*x*y
print("∂f/∂y =", diff(f, y))   # x**2 + 3*y**2

# Mixed partial: ∂²f/∂x∂y = 2x
print("∂²f/∂x∂y =", diff(f, x, y))  # 2*x
