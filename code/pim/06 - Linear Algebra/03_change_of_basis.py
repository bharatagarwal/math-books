# uv run --with numpy python \
#   "code/pim/06 - Linear Algebra/03_change_of_basis.py"
#
# Chapter 10, Section 10.6: change of basis and conjugation.
# Kun's running example: V = R^2 with the target basis
#   v1 = (3, 4), v2 = (-1, -5).
# The change-of-basis matrix P has the v_i as columns, and
# y = P^{-1} x gives the coordinates of x in that basis.

import numpy as np

P = np.array([[3.0, -1.0],
              [4.0, -5.0]])          # columns are v1, v2
Pinv = np.linalg.inv(P)

# Express x = (1, 0) in the basis {v1, v2}. Kun solved the system
#   3a - b = 1,  4a - 5b = 0   to get a = 5/11, b = 4/11.
x = np.array([1.0, 0.0])
coords = Pinv @ x
assert np.allclose(coords, [5 / 11, 4 / 11])
print("(1,0) in basis {v1,v2} =", coords, " (Kun: 5/11, 4/11)")

# Sanity: scaling the v_i by those coordinates rebuilds x.
assert np.allclose(coords[0] * P[:, 0] + coords[1] * P[:, 1], x)

# --- Conjugation: B = P^{-1} A P expresses A in the new basis ---
# A is a "shear" in the standard basis. Pick a vector w given in
# v-coordinates; P^{-1} A P w applies A but stays in v-coordinates.
A = np.array([[1.0, 2.0],
              [0.0, 1.0]])
B = Pinv @ A @ P                     # A, viewed in the {v1,v2} basis

for _ in range(1000):
    w_vcoords = np.random.randn(2)           # w in v-coordinates
    w_std = P @ w_vcoords                     # same vector, std coords
    # Apply A in standard coords, then read off v-coordinates...
    left = Pinv @ (A @ w_std)
    # ...must equal applying the conjugated matrix directly.
    right = B @ w_vcoords
    assert np.allclose(left, right)
print("P^-1 A P reproduces A in the new basis: 1000 vectors agree")

# Conjugation preserves the "fingerprint" of a linear map:
# trace and determinant are basis-independent (similar matrices).
assert np.isclose(np.trace(A), np.trace(B))
assert np.isclose(np.linalg.det(A), np.linalg.det(B))
print("trace(A)=trace(B)=%.3f  det(A)=det(B)=%.3f"
      % (np.trace(B), np.linalg.det(B)))
print("Same map, two perspectives -- not 'similar', identical.")
