# uv run --with numpy python \
#   "code/pim/07 - Eigenvectors and Eigenvalues/02_invariance.py"
# Theorem 12.2: eigenvalues are invariant under a change of basis.
# If B = U A U^{-1}, then A and B have the same eigenvalues, and if v
# is an eigenvector of A then Uv is an eigenvector of B (same lambda).
# Bonus: trace = sum of eigenvalues, det = product of eigenvalues.
import numpy as np

rng = np.random.default_rng(0)
A = rng.integers(-3, 4, size=(4, 4)).astype(float)

# A random invertible change-of-basis matrix U.
U = rng.integers(-2, 3, size=(4, 4)).astype(float)
while abs(np.linalg.det(U)) < 1e-6:
    U = rng.integers(-2, 3, size=(4, 4)).astype(float)
B = U @ A @ np.linalg.inv(U)

eig_A = np.sort(np.linalg.eigvals(A))
eig_B = np.sort(np.linalg.eigvals(B))
print("eig(A) =", np.round(eig_A, 4))
print("eig(B) =", np.round(eig_B, 4))
assert np.allclose(eig_A, eig_B), "eigenvalues must be basis-invariant"
print("Eigenvalues of A and B agree -> Theorem 12.2.")

# Take an eigenvector v of A; check Uv is an eigenvector of B.
vals, vecs = np.linalg.eig(A)
lam, v = vals[0], vecs[:, 0]
vp = U @ v
assert np.allclose(B @ vp, lam * vp), "Uv must be an eigenvector of B"
print("Uv is an eigenvector of B with the same eigenvalue.")

# trace = sum of eigenvalues; det = product of eigenvalues.
print("\ntrace(A) =", round(np.trace(A), 4),
      " sum(eig) =", round(np.sum(eig_A).real, 4))
print("det(A)   =", round(np.linalg.det(A), 4),
      " prod(eig) =", round(np.prod(eig_A).real, 4))
assert np.isclose(np.trace(A), np.sum(eig_A).real)
assert np.isclose(np.linalg.det(A), np.prod(eig_A).real)
print("trace = sum and det = product of eigenvalues.")
