# uv run --with numpy python \
#   "code/bradfield/07-linear-algebra/05_determinant.py"
# 3Blue1Brown, Essence of Linear Algebra, ch 6 (The
# determinant). The determinant is the FACTOR by which a
# transform scales area: the unit square (area 1) becomes a
# parallelogram of area |det|. Negative det = orientation
# flipped. det = 0 = everything squished to a lower dimension.
import numpy as np

# Scale x by 3, y by 2: the unit square becomes a 3-by-2 box,
# area 6. det should report exactly that factor.
scale = np.array([[3.0, 0.0],
                  [0.0, 2.0]])
assert np.isclose(np.linalg.det(scale), 6.0)

# A shear slides the top of the square sideways but keeps the
# base and height -- area is unchanged, so det = 1.
shear = np.array([[1.0, 1.0],
                  [0.0, 1.0]])
assert np.isclose(np.linalg.det(shear), 1.0)

# For 2x2, det = a*d - b*c. Verify against numpy.
a, b, c, d = 2.0, 1.0, 1.0, 3.0
M = np.array([[a, b], [c, d]])
assert np.isclose(np.linalg.det(M), a * d - b * c)

# Negative determinant: this flips orientation (i-hat and
# j-hat swap handedness). |det| is still the area factor.
flip = np.array([[1.0, 0.0],
                 [0.0, -1.0]])
assert np.isclose(np.linalg.det(flip), -1.0)

# det = 0: columns are dependent, the plane collapses onto a
# line -- area becomes 0. This is the non-invertible case.
squish = np.array([[1.0, 2.0],
                   [2.0, 4.0]])
assert np.isclose(np.linalg.det(squish), 0.0)

print("det(scale 3,2) =", np.linalg.det(scale), "(area factor)")
print("det(shear)     =", np.linalg.det(shear), "(area kept)")
print("det(flip)      =", np.linalg.det(flip), "(orientation)")
print("det(squish)    =", round(np.linalg.det(squish)),
      "(collapsed to a line)")
