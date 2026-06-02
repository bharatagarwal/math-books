# uv run --with numpy --with sympy python "code/pim/08 - Multivariable Calculus and Optimization/05_hessian_classify.py"
#
# Theorem 14.18: the eigenvalues of the Hessian classify a critical point.
#   all positive  -> local min
#   all negative  -> local max
#   mixed signs   -> saddle
# We build the Hessian symbolically, then read off eigenvalue signs at a
# critical point.  The saddle case is Kun's example f(x,y) = x^2 - y^2.
import numpy as np
import sympy as sp

x, y = sp.symbols("x y", real=True)


def classify(expr, at):
    grad = [sp.diff(expr, v) for v in (x, y)]
    crit = sp.solve(grad, [x, y], dict=True)
    assert any(s[x] == at[0] and s[y] == at[1] for s in crit), \
        "given point is not actually a critical point"
    H = sp.hessian(expr, (x, y)).subs({x: at[0], y: at[1]})
    eig = np.linalg.eigvalsh(np.array(H, dtype=float))
    if (eig > 0).all():
        return "local min", eig
    if (eig < 0).all():
        return "local max", eig
    return "saddle point", eig


cases = {
    "x^2 + y^2 (bowl)": (x ** 2 + y ** 2, (0, 0), "local min"),
    "-(x^2) - y^2 (dome)": (-x ** 2 - y ** 2, (0, 0), "local max"),
    "x^2 - y^2 (saddle)": (x ** 2 - y ** 2, (0, 0), "saddle point"),
}

for name, (expr, at, want) in cases.items():
    got, eig = classify(expr, at)
    print(f"{name:<22} eig={np.round(eig, 3)} -> {got}")
    assert got == want, (name, got, want)

print("Hessian eigenvalue signs classify every critical point.")
