# uv run --with sympy python "code/pim/08 - Multivariable Calculus and Optimization/02_gradient_symbolic.py"
#
# Verify Kun's running gradient example:
#   f(x1, x2, x3) = x1^2 * x2 + cos(x3)
#   grad f = ( 2 x1 x2,  x1^2,  -sin(x3) )
# and the directional derivative he computes at x = (1, 2, pi/2)
# in the direction of an unspecified unit vector v.
import sympy as sp

x1, x2, x3, v1, v2, v3 = sp.symbols("x1 x2 x3 v1 v2 v3", real=True)
f = x1 ** 2 * x2 + sp.cos(x3)

grad = sp.Matrix([sp.diff(f, v) for v in (x1, x2, x3)]).T
expected = sp.Matrix([[2 * x1 * x2, x1 ** 2, -sp.sin(x3)]])
assert sp.simplify(grad - expected) == sp.zeros(1, 3)
print("grad f =", grad.tolist()[0])

# Directional derivative as the inner product <grad f, v>, with the
# point fixed at (1, 2, pi/2) and the direction v = (v1, v2, v3) free.
v = sp.Matrix([v1, v2, v3])
grad_at = grad.subs({x1: 1, x2: 2, x3: sp.pi / 2})
dir_deriv = sp.simplify((grad_at * v)[0])
print("grad f(1, 2, pi/2) =", grad_at.tolist()[0])
print("Dir(f, x, v) =", dir_deriv)

# Kun's answer: grad = (4, 1, -1), and Dir = 4 v1 + v2 - v3.
assert grad_at.tolist()[0] == [4, 1, -1]
assert sp.simplify(dir_deriv - (4 * v1 + v2 - v3)) == 0
print("Matches Kun: (4  1  -1) and 4*v1 + v2 - v3.")
