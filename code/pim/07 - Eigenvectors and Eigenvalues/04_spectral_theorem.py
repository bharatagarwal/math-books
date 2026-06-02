# uv run --with numpy python \
#   "code/pim/07 - Eigenvectors and Eigenvalues/04_spectral_theorem.py"
# The Spectral Theorem (12.22): a real matrix is symmetric iff it has
# an orthonormal basis of eigenvectors. We verify both consequences:
#  (1) a symmetric matrix has REAL eigenvalues and ORTHONORMAL
#      eigenvectors, giving the factorization A = Q Lambda Q^T;
#  (2) a non-symmetric matrix can fail to have real eigenvalues.
import numpy as np

rng = np.random.default_rng(7)
M = rng.standard_normal((5, 5))
A = (M + M.T) / 2  # force symmetry: A = A^T

# eigh is the symmetric solver: it returns real eigenvalues and an
# orthonormal eigenvector matrix Q (Q^T Q = I).
vals, Q = np.linalg.eigh(A)
print("eigenvalues (all real):", np.round(vals, 4))
assert np.allclose(vals, vals.real), "symmetric => real eigenvalues"

# Q's columns are pairwise orthonormal (Propositions 12.11 + 12.14).
assert np.allclose(Q.T @ Q, np.eye(5), atol=1e-12)
print("Q^T Q = I: eigenvectors form an orthonormal basis.")

# Diagonalization: A = Q Lambda Q^T.
Lam = np.diag(vals)
assert np.allclose(Q @ Lam @ Q.T, A, atol=1e-12)
print("A = Q Lambda Q^T reconstructs A exactly.")

# Proposition 12.16: for an orthonormal Q, the inverse is the
# transpose, so Q^T = Q^{-1}.
assert np.allclose(Q.T, np.linalg.inv(Q), atol=1e-10)
print("Q^T = Q^{-1} (orthonormal change of basis).")

# Contrast: a rotation by pi/4 is NOT symmetric and has no real
# eigenvalues -- exactly Kun's "rotation has no eigenvalues" remark.
t = np.pi / 4
R = np.array([[np.cos(t), -np.sin(t)],
              [np.sin(t), np.cos(t)]])
r_vals = np.linalg.eigvals(R)
print("\nrotation eigenvalues:", np.round(r_vals, 4))
assert np.all(np.abs(r_vals.imag) > 1e-6), "rotation: complex eigvals"
print("Rotation has complex eigenvalues -> not symmetric, no real ones.")
