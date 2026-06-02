# uv run --with numpy python "code/pim/09 - Groups/07_orthogonal_group.py"
"""The orthogonal group O(2): isometries of the plane fixing the origin.

Theorem 16.13 says the distance-preserving linear maps are exactly
those whose columns are orthonormal, i.e. A^T A = I. We:
  1. confirm a rotation and a reflection satisfy A^T A = I and preserve
     distance d(Ax, Ay) = d(x, y);
  2. confirm O(2) is closed under products and inverses (it's a group);
  3. confirm a generic invertible matrix is NOT an isometry.
This is Kun's invariant-first view of Euclidean geometry in code.
"""
import numpy as np

rng = np.random.default_rng(2)


def is_orthogonal(A):
    return np.allclose(A.T @ A, np.eye(A.shape[0]))


def preserves_distance(A, trials=2000):
    for _ in range(trials):
        x, y = rng.uniform(-10, 10, (2, 2))
        d0 = np.linalg.norm(x - y)
        d1 = np.linalg.norm(A @ x - A @ y)
        if not np.isclose(d0, d1):
            return False
    return True


def rotation(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, -s], [s, c]])


reflection = np.array([[1.0, 0.0], [0.0, -1.0]])  # flip across x-axis
R = rotation(np.pi / 3)

for name, A in [("rotation(60deg)", R), ("reflection", reflection)]:
    assert is_orthogonal(A), name
    assert preserves_distance(A), name
    print(f"{name}: A^T A = I and it preserves all distances.")

# Closure: product and inverse of orthogonal matrices stay orthogonal.
assert is_orthogonal(R @ reflection)
assert is_orthogonal(np.linalg.inv(R))
print("O(2) is closed under products and inverses: it is a group.")

# A shear is invertible but NOT orthogonal, and distorts distances.
shear = np.array([[1.0, 2.0], [0.0, 1.0]])
assert not is_orthogonal(shear)
assert not preserves_distance(shear)
print("A shear is invertible but not orthogonal -- not an isometry.")
