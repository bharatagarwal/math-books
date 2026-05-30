# uv run --with numpy python \
#   "code/bradfield/07-linear-algebra/06_inverse_rank.py"
# 3Blue1Brown, Essence of Linear Algebra, ch 7 (Inverse
# matrices, column space, null space). Solving A x = v means
# "which vector x lands on v?" If det != 0 there is a unique
# answer, found by the inverse: x = A^-1 v. If det = 0 the
# transform squished space and the inverse cannot exist.
import numpy as np

A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
v = np.array([4.0, 5.0])

# det != 0, so A is invertible and A x = v has one solution.
assert not np.isclose(np.linalg.det(A), 0.0)
x = np.linalg.solve(A, v)
assert np.allclose(A @ x, v)            # x really lands on v
assert np.allclose(np.linalg.inv(A) @ A, np.eye(2))  # undo
print("solve A x = v:  x =", x)
print("check A @ x  =", A @ x, "(== v)")

# Rank = dimension of the column space = number of dimensions
# in the OUTPUT. Full-rank 2x2 spans the whole plane.
assert np.linalg.matrix_rank(A) == 2
print("rank(A) =", np.linalg.matrix_rank(A), "(full -> the "
      "output fills the plane)")

# A squishing matrix has det 0, rank 1 (output is a line),
# and a non-trivial NULL SPACE: vectors sent to the origin.
S = np.array([[1.0, 2.0],
              [2.0, 4.0]])
assert np.isclose(np.linalg.det(S), 0.0)
assert np.linalg.matrix_rank(S) == 1
null_vec = np.array([2.0, -1.0])        # lands on (0,0)
assert np.allclose(S @ null_vec, np.zeros(2))
print("rank(S) =", np.linalg.matrix_rank(S),
      "(squished to a line)")
print("null space vector (2,-1) -> S @ it =", S @ null_vec)
