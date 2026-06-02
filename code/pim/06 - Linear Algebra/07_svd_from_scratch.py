# uv run --with numpy python \
#   "code/pim/06 - Linear Algebra/07_svd_from_scratch.py"
#
# Chapter 10, Section 10.9: "Code It Up." This is Kun's greedy svd()
# built on top of the power-method svd_1d. It computes one singular
# triple at a time, then subtracts off the rank-1 outer product
# sigma * outer(u, v) so the next round sees only the leftover signal.

from math import sqrt
from random import normalvariate, seed

import numpy as np

seed(0)
np.random.seed(0)


def random_unit_vector(n):
    u = [normalvariate(0, 1) for _ in range(n)]
    norm = sqrt(sum(x * x for x in u))
    return [x / norm for x in u]


def svd_1d(A, epsilon=1e-10):
    n, m = A.shape
    current_v = random_unit_vector(min(n, m))
    B = np.dot(A.T, A) if n > m else np.dot(A, A.T)
    while True:
        last_v = current_v
        current_v = np.dot(B, last_v)
        current_v = current_v / np.linalg.norm(current_v)
        if abs(np.dot(current_v, last_v)) > 1 - epsilon:
            return current_v


def svd(A, k=None, epsilon=1e-10):
    A = np.array(A, dtype=float)
    n, m = A.shape
    svd_so_far = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrix_for_1d = A.copy()
        for singular_value, u, v in svd_so_far[:i]:
            matrix_for_1d -= singular_value * np.outer(u, v)

        if n > m:
            v = svd_1d(matrix_for_1d, epsilon)   # next singular vec
            u_unnormalized = np.dot(A, v)
            sigma = np.linalg.norm(u_unnormalized)
            u = u_unnormalized / sigma
        else:
            u = svd_1d(matrix_for_1d, epsilon)
            v_unnormalized = np.dot(A.T, u)
            sigma = np.linalg.norm(v_unnormalized)
            v = v_unnormalized / sigma
        svd_so_far.append((sigma, u, v))

    singular_values, us, vs = [np.array(x) for x in zip(*svd_so_far)]
    return singular_values, us.T, vs


# Movie ratings (Figure 10.9): rows movies, columns people.
A = np.array([
    [2, 5, 3],
    [1, 2, 1],
    [4, 1, 1],
    [3, 5, 2],
    [5, 3, 1],
    [4, 5, 5],
    [2, 4, 2],
    [2, 2, 5],
], dtype=float)

sigmas, U, V = svd(A)
print("singular values from scratch:", np.round(sigmas, 4))

# Compare with numpy: singular values are basis-independent, so they
# must match exactly (up to numerical noise).
_, S_true, _ = np.linalg.svd(A)
assert np.allclose(sorted(sigmas, reverse=True),
                   sorted(S_true, reverse=True), atol=1e-6)
print("match numpy singular values:", np.round(S_true, 4))

# Reconstruct A = U Sigma V^T from our own pieces.
reconstructed = (U * sigmas) @ V
assert np.allclose(reconstructed, A, atol=1e-6)
print("U Sigma V^T rebuilds the rating matrix exactly")
