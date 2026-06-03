# uv run --with sympy python
# Function notation in Python: f: A -> B is a type hint,
# composition g∘f is nesting, x ↦ y is a lambda.
from typing import Callable
import sympy as sp

# --- f: R -> R as a type signature ---
def f(x: float) -> float:
    """f: R -> R defined by f(x) = x^2 + 1"""
    return x ** 2 + 1

print(f"f(3) = {f(3)}")         # f(3) = 10
print(f"f(-2) = {f(-2)}")       # f(-2) = 5

# --- x ↦ y via lambda (anonymous functions) ---
g: Callable[[float], float] = lambda x: 2 * x + 3
print(f"g(4) = {g(4)}")         # g(4) = 11

# --- Composition: (g ∘ f)(x) = g(f(x)) ---
def compose(g, f):
    """g ∘ f: returns a new function"""
    return lambda x: g(f(x))

gf = compose(g, f)              # g ∘ f
fg = compose(f, g)              # f ∘ g (different!)
print(f"(g∘f)(3) = g(f(3)) = g(10) = {gf(3)}")
print(f"(f∘g)(3) = f(g(3)) = {fg(3)}")
# Composition is NOT commutative: 23 ≠ 82

# --- SymPy: symbolic composition ---
x = sp.Symbol('x')
f_sym = x**2 + 1
g_sym = 2*x + 3
composed = g_sym.subs(x, f_sym)
print(f"\ng(f(x)) = {sp.expand(composed)}")
# g(f(x)) = 2*x**2 + 5

# --- Inverse: f^{-1} via SymPy solve ---
y = sp.Symbol('y')
inv = sp.solve(sp.Eq(y, x**2 + 1), x)
print(f"f(x) = x² + 1, so f⁻¹(y) = {inv}")
# Two branches: [-sqrt(y-1), sqrt(y-1)]
# Not a function unless we restrict the domain!
