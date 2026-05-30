# uv run --with numpy python \
#   code/bradfield/08-linear-algebra-2/06_projection_error.py
#
# INTUITION DEMO: least squares IS projection. b lives in R^3;
# the column space of A is a 2D plane through the origin. The
# best fit Ax* is the foot of the perpendicular from b to that
# plane -- the closest point. We *watch* the squared error
# ||Ax - b||^2 shrink as we slide x toward x*, and bottom out
# exactly at the projection, where the residual is orthogonal.
import numpy as np

# Two columns spanning a plane in R^3, and an off-plane target.
A = np.array([[1.0, 0.0],
              [0.0, 1.0],
              [1.0, 1.0]])
b = np.array([2.0, 1.0, 5.0])  # not in the plane

x_star, *_ = np.linalg.lstsq(A, b, rcond=None)
proj = A @ x_star
err_star = np.linalg.norm(proj - b) ** 2
print(f"best x* = {x_star},  projection A x* = {proj}")
print(f"minimum squared error = {err_star:.4f}\n")

# Slide x along the line from a poor guess to x* and print the
# error collapsing to the minimum at t = 1.
x_bad = x_star + np.array([1.5, -1.2])
print(" t   x(t)                 ||A x - b||^2")
prev = None
for t in [0.0, 0.25, 0.5, 0.75, 1.0]:
    x = x_bad + t * (x_star - x_bad)
    err = np.linalg.norm(A @ x - b) ** 2
    if prev is not None:
        assert err <= prev + 1e-9  # monotone down to the foot
    prev = err
    print(f"{t:4.2f} {np.round(x,3)!s:>20}  {err:10.4f}")

assert np.isclose(prev, err_star)
# Perpendicularity: the winning residual is orthogonal to BOTH
# columns of A (it sticks straight out of the plane).
resid = b - proj
for j in range(A.shape[1]):
    assert abs(A[:, j] @ resid) < 1e-9
print("\nat the bottom the residual is perpendicular to the plane")
print("(A^T (b - A x*) = 0) -- that is what 'closest' means")
