# uv run --with numpy python \
#   "code/pim/07 - Eigenvectors and Eigenvalues/05_orthonormal_basis.py"
# Orthonormal bases (Section 12.4). Proposition 12.15: in an
# orthonormal basis the coefficient of v_i is just the inner product
# <x, v_i>. No linear system to solve -- contrast Gaussian elimination.
# We build an orthonormal basis with Gram-Schmidt and check both.
import numpy as np


def gram_schmidt(vectors):
    """Orthonormalize a list of vectors (Section 12.4)."""
    basis = []
    for v in vectors:
        w = v.astype(float).copy()
        for b in basis:  # subtract projections onto prior basis vecs
            w = w - (w @ b) * b
        basis.append(w / np.linalg.norm(w))
    return np.array(basis)


rng = np.random.default_rng(3)
raw = [rng.standard_normal(4) for _ in range(4)]
V = gram_schmidt(raw)  # rows are the orthonormal basis vectors v_i

# Verify orthonormality: <v_i, v_j> = 1 if i==j else 0.
G = V @ V.T
assert np.allclose(G, np.eye(4), atol=1e-12)
print("Gram-Schmidt produced an orthonormal basis (V V^T = I).")

# Pick a target vector x and represent it in this basis.
x = rng.standard_normal(4)

# Method 1 (Prop 12.15): coefficient of v_i is the inner product.
coeffs_inner = V @ x  # n inner products, O(n^2) total

# Method 2: solve the linear system A y = x, columns of A are the v_i.
A = V.T
coeffs_solve = np.linalg.solve(A, x)  # Gaussian elimination, O(n^3)

print("coeffs via inner products:", np.round(coeffs_inner, 4))
print("coeffs via linear solve:  ", np.round(coeffs_solve, 4))
assert np.allclose(coeffs_inner, coeffs_solve, atol=1e-10)
print("Both agree -- the inner product shortcut works.")

# Reconstruct x = sum_i <x, v_i> v_i and confirm we recover x.
x_rebuilt = coeffs_inner @ V
assert np.allclose(x_rebuilt, x, atol=1e-12)
print("x = sum_i <x,v_i> v_i reconstructs x exactly.")
