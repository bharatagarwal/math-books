# uv run --with numpy python \
#   "code/pim/07 - Eigenvectors and Eigenvalues/03_power_iteration.py"
# Computing eigenvalues: power iteration. Repeatedly applying a matrix
# and renormalizing drives any generic start vector toward the
# eigenvector of the *largest-magnitude* eigenvalue. This is exactly
# the "rescale before and after multiplying by A" invariance Kun
# describes -- A sends the dominant eigenvector back to itself.
import numpy as np


def power_iteration(A, steps=200, seed=1):
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(A.shape[0])
    v /= np.linalg.norm(v)
    for _ in range(steps):
        w = A @ v
        v = w / np.linalg.norm(w)
    # Rayleigh quotient gives the eigenvalue for this eigenvector.
    lam = v @ (A @ v)
    return lam, v


# A symmetric matrix, so eigenvalues are real (Spectral Theorem).
A = np.array([[2.0, 1.0, 0.0],
              [1.0, 3.0, 1.0],
              [0.0, 1.0, 2.0]])

lam, v = power_iteration(A)
print("power-iteration eigenvalue:", round(lam, 6))

# Compare against the exact dominant eigenpair from a direct solver.
vals, vecs = np.linalg.eigh(A)
dom = np.argmax(np.abs(vals))
lam_true = vals[dom]
v_true = vecs[:, dom]
print("exact dominant eigenvalue: ", round(lam_true, 6))
assert np.isclose(lam, lam_true, atol=1e-6)

# Eigenvectors are defined up to sign; align before comparing.
if v @ v_true < 0:
    v = -v
print("eigenvector error:", round(np.linalg.norm(v - v_true), 8))
assert np.allclose(v, v_true, atol=1e-6)

# Av = lambda v is the definition (Definition 12.1) -- confirm it.
assert np.allclose(A @ v, lam * v, atol=1e-6)
print("A v = lambda v holds to 1e-6: power iteration converged.")
