# uv run --with numpy python \
#   code/bradfield/08-linear-algebra-2/02_least_squares.py
#
# More equations than unknowns: 60 noisy points, 2 line params.
# Ax = b has no exact solution, so find x minimizing
# ||Ax - b||^2. Two routes -- the normal equations
# A^T A x = A^T b and numpy's stable lstsq -- must agree and
# recover the true line y = 2x + 1.
import numpy as np

rng = np.random.default_rng(0)
n = 60
xs = np.linspace(0.0, 10.0, n)
true_slope, true_intercept = 2.0, 1.0
ys = true_slope * xs + true_intercept + rng.normal(0, 1.0, n)

# Design matrix: column of x's and a column of ones.
A = np.column_stack([xs, np.ones(n)])
b = ys

# Route 1: normal equations A^T A x = A^T b.
normal = np.linalg.solve(A.T @ A, A.T @ b)

# Route 2: numpy's least-squares solver.
lstsq, *_ = np.linalg.lstsq(A, b, rcond=None)

assert np.allclose(normal, lstsq, atol=1e-9)
print(f"normal equations: slope={normal[0]:.3f} intercept={normal[1]:.3f}")
print(f"numpy lstsq     : slope={lstsq[0]:.3f} intercept={lstsq[1]:.3f}")
assert abs(normal[0] - true_slope) < 0.2
assert abs(normal[1] - true_intercept) < 0.6
print(f"recovered true line y = {true_slope}x + {true_intercept}")

# Geometry: the residual b - Ax is orthogonal to the column
# space, i.e. A^T (b - Ax) = 0. That is exactly the normal
# equations rearranged -- the error is perpendicular.
resid = b - A @ normal
assert np.allclose(A.T @ resid, [0.0, 0.0], atol=1e-9)
print("residual is orthogonal to the column space (A^T r = 0)")
