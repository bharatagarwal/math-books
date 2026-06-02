# uv run --with sympy python \
#   "code/pim/05 - Calculus with One Variable/05_newton_quadratic.py"
# Newton's method on f(x) = x^5 - x - 1, the chapter's example whose
# root has no algebraic formula (Abel-Ruffini). The update is
#   x_{n+1} = x_n - f(x_n)/f'(x_n)   (rearranged degree-1 Taylor poly).
# Theorem 8.15 promises QUADRATIC convergence: the error roughly
# squares each step (the count of correct digits doubles). We watch
# e_{n+1} <= C * e_n^2 hold, and match sympy's high-precision root.
import sympy as sp

x = sp.Symbol("x")
f_expr = x**5 - x - 1
f = sp.lambdify(x, f_expr, "math")
fp = sp.lambdify(x, sp.diff(f_expr, x), "math")

# Ground-truth root to 30 digits from sympy.
root = sp.nsolve(f_expr, x, 1.0, prec=30)
r = float(root)
print(f"sympy root r = {root}")


def newton(start, steps=8):
    xn = start
    for _ in range(steps):
        yield xn
        xn = xn - f(xn) / fp(xn)


prev_err = None
ratio = None
for n, xn in enumerate(newton(1.0)):
    err = abs(xn - r)
    line = f"x_{n} = {xn:.16f}  f(x_n)={f(xn):+.2e}  e_n={err:.2e}"
    if prev_err and prev_err < 1 and prev_err > 1e-14:
        ratio = err / prev_err**2          # e_{n+1} / e_n^2
        line += f"  e_n/e_(n-1)^2={ratio:.3f}"
    print(line)
    prev_err = err

# Newton matched sympy's root to floating-point precision.
final = list(newton(1.0, steps=8))[-1]
assert abs(final - r) < 1e-12
# The error ratio stayed bounded -> quadratic (not just linear).
assert ratio is not None and ratio < 5
print(f"\nConverged to {final:.16f}; e_(n+1)/e_n^2 bounded "
      f"=> quadratic convergence.")
