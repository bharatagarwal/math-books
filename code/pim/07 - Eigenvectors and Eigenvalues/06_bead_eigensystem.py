# uv run --with numpy python \
#   "code/pim/07 - Eigenvectors and Eigenvalues/06_bead_eigensystem.py"
# The Waves application (Section 12.7). The 5-bead string gives the
# symmetric tridiagonal matrix A with -2 on the diagonal and 1 on the
# off-diagonals. We reproduce Kun's Figure 12.9 eigensystem table.
import numpy as np


def shift(lst, k):
    """Cyclic-free shift of a base row by k positions (zero-padded)."""
    n = len(lst)
    out = [0] * n
    for i, val in enumerate(lst):
        j = i + k
        if 0 <= j < n:
            out[j] = val
    return out


def bead_matrix(dimension=5):
    base = [1, -2, 1] + [0] * (dimension - 3)
    return np.array([shift(base, i) for i in range(-1, dimension - 1)])


def sorted_eigensystem(matrix, top_k=None):
    top_k = top_k or len(matrix)
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    idx = eigenvalues.argsort()[::-1]  # largest eigenvalue first
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    # return eigenvectors as ROWS, matching Kun's convention
    return eigenvalues[:top_k], eigenvectors.T[:top_k]


A = bead_matrix(5)
print("bead matrix A =")
print(A)
assert np.allclose(A, A.T), "the bead matrix is symmetric"

eigenvalues, eigenvectors = sorted_eigensystem(A)
print("\nFigure 12.9 table (eigenvalue : eigenvector):")
for lam, vec in zip(eigenvalues, eigenvectors):
    print(f"{lam:6.2f} : {np.round(vec, 2)}")

# Kun's table lists these five eigenvalues for the 5-bead system.
expected = np.array([-0.27, -1.00, -2.00, -3.00, -3.73])
assert np.allclose(eigenvalues, expected, atol=0.01)
print("\nEigenvalues match Kun's Figure 12.9 to two decimals.")

# The eigenvectors are orthonormal (Spectral Theorem) and each one
# really satisfies A v = lambda v.
assert np.allclose(eigenvectors @ eigenvectors.T, np.eye(5), atol=1e-12)
for lam, vec in zip(eigenvalues, eigenvectors):
    assert np.allclose(A @ vec, lam * vec, atol=1e-12)
print("All five are orthonormal eigenvectors: A v = lambda v.")
