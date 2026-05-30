# uv run --with numpy python \
#   "code/bradfield/07-linear-algebra/03_matrices_as_maps.py"
# 3Blue1Brown, Essence of Linear Algebra, ch 3 (Linear
# transformations and matrices). The columns of a matrix are
# exactly WHERE THE BASIS VECTORS LAND. Applying the matrix
# to (x,y) = x*(new i-hat) + y*(new j-hat).
import numpy as np

# A 90-degree counter-clockwise rotation.
#   i-hat = (1,0) -> (0,1)   (first column)
#   j-hat = (0,1) -> (-1,0)  (second column)
R = np.array([[0.0, -1.0],
              [1.0,  0.0]])

ihat, jhat = np.array([1.0, 0.0]), np.array([0.0, 1.0])
assert np.array_equal(R @ ihat, R[:, 0])  # land of i-hat
assert np.array_equal(R @ jhat, R[:, 1])  # land of j-hat

# A general vector follows its basis vectors: the transform
# is linear, so M@(x*ihat + y*jhat) = x*M@ihat + y*M@jhat.
v = np.array([3.0, 1.0])
by_columns = v[0] * R[:, 0] + v[1] * R[:, 1]
assert np.allclose(R @ v, by_columns)
print("R @ v          =", R @ v)
print("x*col0+y*col1  =", by_columns, "(same thing)")

# A shear keeps i-hat fixed and slides j-hat to (1,1).
shear = np.array([[1.0, 1.0],
                  [0.0, 1.0]])
assert np.array_equal(shear @ ihat, np.array([1.0, 0.0]))
assert np.array_equal(shear @ jhat, np.array([1.0, 1.0]))
print("shear sends j-hat to", shear @ jhat)
print("a matrix is read column-by-column as basis landings")
