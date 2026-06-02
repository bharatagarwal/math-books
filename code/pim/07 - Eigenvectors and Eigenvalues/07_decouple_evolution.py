# uv run --with numpy python \
#   "code/pim/07 - Eigenvectors and Eigenvalues/07_decouple_evolution.py"
# The payoff of an orthonormal eigenbasis: a coupled system decouples.
# Pluck bead 2, y(0) = (0, 0.5, 0, 0, 0). We decompose y(0) into the
# eigenbasis (Prop 12.15), evolve each coefficient as an independent
# cosine z_i(t) = z_i(0) cos(sqrt(-lambda_i) t), and convert back.
import numpy as np


def shift(lst, k):
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


def sorted_eigensystem(matrix):
    vals, vecs = np.linalg.eigh(matrix)
    idx = vals.argsort()[::-1]
    return vals[idx], vecs[:, idx].T  # eigenvectors as rows


def decompose(eigenvectors, vector):
    """Coefficient on each eigenvector = inner product (Prop 12.15)."""
    return np.array([np.dot(vector, ev) for ev in eigenvectors])


A = bead_matrix(5)
eigenvalues, eigenvectors = sorted_eigensystem(A)

y0 = np.array([0.0, 0.5, 0.0, 0.0, 0.0])  # pluck the middle-ish bead
coeffs = decompose(eigenvectors, y0)
print("eigenbasis coefficients of y(0):", np.round(coeffs, 3))

# Reconstruct y(0) from the coefficients -- a sanity check that the
# decomposition is exact (orthonormal basis, so no information lost).
y0_rebuilt = coeffs @ eigenvectors
assert np.allclose(y0_rebuilt, y0, atol=1e-12)
print("reconstructed y(0):", np.round(y0_rebuilt, 3))


def state_at(t):
    """y(t): each mode is a cosine; recombine in the bead basis.
    z_i'' = lambda_i z_i with z_i'(0)=0  =>  z_i(t)=z_i(0)cos(w_i t),
    where w_i = sqrt(-lambda_i) since the lambda_i are negative."""
    omegas = np.sqrt(-eigenvalues)
    z = coeffs * np.cos(omegas * t)
    return z @ eigenvectors


# At t = 0 we must recover y(0) exactly.
assert np.allclose(state_at(0.0), y0, atol=1e-12)

# Cross-check the decoupled solution against directly integrating the
# coupled ODE y'' = A y with a tiny leapfrog (Stoermer-Verlet) step.
def integrate(t_final, dt=1e-4):
    y = y0.copy()
    v = np.zeros(5)        # zero initial velocity (plucked and released)
    steps = int(round(t_final / dt))
    for _ in range(steps):
        v = v + 0.5 * dt * (A @ y)
        y = y + dt * v
        v = v + 0.5 * dt * (A @ y)
    return y


for t in [0.5, 1.0, 2.0]:
    closed = state_at(t)
    numeric = integrate(t)
    err = np.linalg.norm(closed - numeric)
    print(f"t={t}:  decoupled={np.round(closed, 4)}  err={err:.2e}")
    assert err < 1e-3, "decoupled formula must match the coupled ODE"

print("\nDecoupled cosine modes reproduce the coupled dynamics.")
