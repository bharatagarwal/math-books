# uv run --with numpy python \
#   "code/pim/06 - Linear Algebra/05_power_method.py"
#
# Chapter 10, Section 10.9: the power method (Theorem 10.26).
# This is Kun's own svd_1d, lightly trimmed. The one-dimensional
# problem is: find the unit vector v maximizing ||A v||.
# The trick is to repeatedly apply B = A^T A; each application
# "pulls" the iterate toward the top singular vector v1.

from math import sqrt
from random import normalvariate, seed

import numpy as np

seed(0)
np.random.seed(0)


def norm(v):
    return sqrt(sum(x * x for x in v))


def random_unit_vector(n):
    unnormalized = [normalvariate(0, 1) for _ in range(n)]
    the_norm = norm(unnormalized)
    return [x / the_norm for x in unnormalized]


def svd_1d(A, epsilon=1e-10):
    """First singular vector of A via the power method."""
    n, m = A.shape
    x = random_unit_vector(min(n, m))
    last_v = None
    current_v = x

    if n > m:
        B = np.dot(A.T, A)
    else:
        B = np.dot(A, A.T)           # spot check: why is this okay?

    iterations = 0
    while True:
        iterations += 1
        last_v = current_v
        current_v = np.dot(B, last_v)
        current_v = current_v / np.linalg.norm(current_v)
        if abs(np.dot(current_v, last_v)) > 1 - epsilon:
            return current_v, iterations


# Kun's movie-rating matrix (Figure 10.9): rows are movies, columns
# are the people Aisha, Bob, Chandrika.
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

v1, iters = svd_1d(A)
print("power method converged in", iters, "iterations")
print("first singular vector v1 =", np.round(v1, 4))

# Cross-check against numpy's battle-tested SVD. The top right
# singular vector is unique up to sign, so compare |cos angle|.
_, S, Vt = np.linalg.svd(A)
v1_true = Vt[0]
agreement = abs(float(np.dot(v1, v1_true)))
assert agreement > 1 - 1e-6
print("agreement with numpy's v1 (|cos|):", round(agreement, 9))

# The first singular value sigma_1 = ||A v1|| should match too.
sigma_1 = np.linalg.norm(A @ v1)
assert np.isclose(sigma_1, S[0])
print("sigma_1 = ||A v1|| =", round(sigma_1, 6),
      "(numpy:", round(S[0], 6), ")")
