# uv run --with numpy python \
#   "code/pim/06 - Linear Algebra/02_matrix_as_map.py"
#
# Chapter 10, Section 10.5: "A linear map is completely determined by
# its behavior on a basis." (Theorem 10.11.)
# The i-th COLUMN of M(f) is f(e_i) written in the codomain basis.
# So a matrix-vector product just rebuilds f(x) = sum_i a_i f(e_i)
# from the columns. We verify all of this on Kun's 2x3 example.

import numpy as np

# Kun's worked example matrix (page 153):
#   ( 9  2  1 )        ( 3)        (29)
#   ( 7 -2  0 )   times (-1)   ==   (23)
#                       ( 4)
A = np.array([[9, 2, 1],
              [7, -2, 0]])
x = np.array([3, -1, 4])

# By hand, Kun computes 9*3 + 2*(-1) + 1*4 = 29 and
# 7*3 + (-2)*(-1) + 0*4 = 23.
assert list(A @ x) == [29, 23]
print("A x =", A @ x, "(matches Kun's 29, 23)")

# The columns ARE the images of the standard basis vectors.
e1, e2, e3 = np.eye(3)
assert np.array_equal(A @ e1, A[:, 0])  # (9, 7)
assert np.array_equal(A @ e2, A[:, 1])  # (2, -2)
assert np.array_equal(A @ e3, A[:, 2])  # (1, 0)
print("column i of A equals A @ e_i:", A[:, 0], A[:, 1], A[:, 2])

# And f(x) is the linear combination of columns weighted by x's
# coordinates: f(x) = 3*col0 + (-1)*col1 + 4*col2.
rebuilt = 3 * A[:, 0] + (-1) * A[:, 1] + 4 * A[:, 2]
assert np.array_equal(rebuilt, A @ x)
print("rebuilt from columns:", rebuilt)

# Theorem 10.14: composition of maps is matrix multiplication.
# Let f: R^3 -> R^2 be A, and g: R^2 -> R^2 a rotation by 90 deg.
g = np.array([[0, -1],
              [1, 0]])           # (a, b) -> (-b, a)
for _ in range(1000):
    v = np.random.randint(-9, 10, size=3)
    # g(f(v)) computed two ways must agree.
    assert np.array_equal(g @ (A @ v), (g @ A) @ v)
print("M(g o f) = M(g) M(f): 1000 random vectors agree")
