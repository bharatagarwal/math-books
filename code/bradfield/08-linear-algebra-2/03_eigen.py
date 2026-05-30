# uv run --with numpy python \
#   code/bradfield/08-linear-algebra-2/03_eigen.py
#
# Eigenvectors are the directions a map only *scales*, never
# knocks off their line: A v = lambda v. We verify the defining
# equation, then two free invariants -- trace = sum of
# eigenvalues, det = product -- and the spectral theorem for a
# symmetric matrix (real eigenvalues, orthogonal eigenvectors).
import numpy as np

A = np.array([[2.0, 1.0], [1.0, 2.0]])  # symmetric
vals, vecs = np.linalg.eig(A)

# Defining equation, column by column: A v = lambda v.
for i in range(len(vals)):
    v = vecs[:, i]
    assert np.allclose(A @ v, vals[i] * v)
print(f"eigenvalues: {np.sort(vals)}")
for i in range(len(vals)):
    print(f"  A v = {vals[i]:.1f} v  for v = {np.round(vecs[:, i], 3)}")

# trace = sum of eigenvalues, det = product of eigenvalues.
assert np.isclose(np.trace(A), vals.sum())
assert np.isclose(np.linalg.det(A), np.prod(vals))
print(f"trace {np.trace(A):.1f} = sum {vals.sum():.1f}; "
      f"det {np.linalg.det(A):.1f} = prod {np.prod(vals):.1f}")

# Spectral theorem: symmetric -> real eigenvalues, orthogonal
# eigenvectors.
assert np.allclose(vals.imag, 0.0)
assert np.isclose(vecs[:, 0] @ vecs[:, 1], 0.0)
print("symmetric: eigenvalues real, eigenvectors orthogonal")
