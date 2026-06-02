# uv run --with numpy python \
#   "code/pim/06 - Linear Algebra/06_low_rank_approx.py"
#
# Chapter 10, Section 10.9: A = U Sigma V^T, and the "approximation
# aspect of the SVD is to stop at some step k." We rebuild A from
# its top-k singular triples and watch the error drop as k grows --
# this is exactly low-rank approximation / dimensionality reduction.

import numpy as np

np.random.seed(1)


def rank_k_approx(U, S, Vt, k):
    """Reconstruct using only the top k singular triples."""
    return (U[:, :k] * S[:k]) @ Vt[:k, :]


# Build a matrix that is genuinely close to rank 2 (a strong "signal"
# in two directions plus a little noise) so the error curve is vivid.
m, n = 8, 6
signal = np.outer(np.random.randn(m), np.random.randn(n)) * 6
signal += np.outer(np.random.randn(m), np.random.randn(n)) * 3
A = signal + np.random.randn(m, n) * 0.3

U, S, Vt = np.linalg.svd(A, full_matrices=False)
print("singular values:", np.round(S, 3))

# Full reconstruction (k = all) must return A exactly.
full = rank_k_approx(U, S, Vt, len(S))
assert np.allclose(full, A)
print("k = %d  rebuilds A exactly" % len(S))

# Error must be monotonically non-increasing as k grows.
print("\n rank k | reconstruction error ||A - A_k||")
prev = np.inf
for k in range(1, len(S) + 1):
    Ak = rank_k_approx(U, S, Vt, k)
    err = np.linalg.norm(A - Ak)
    print("   %2d   | %10.5f" % (k, err))
    assert err <= prev + 1e-9        # error never goes up
    prev = err

# Eckart-Young: the best rank-k error in Frobenius norm is exactly
# the norm of the discarded singular values. Verify for k = 2.
k = 2
err_k = np.linalg.norm(A - rank_k_approx(U, S, Vt, k))
discarded = np.linalg.norm(S[k:])
assert np.isclose(err_k, discarded)
print("\nbest rank-2 error = ||discarded sigmas|| = %.5f" % discarded)
print("(Eckart-Young: truncating the SVD IS the best approximation)")
