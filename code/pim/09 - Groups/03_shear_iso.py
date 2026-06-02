# uv run --with numpy python "code/pim/09 - Groups/03_shear_iso.py"
"""(R, +) is isomorphic to the group of horizontal shear matrices.

Kun's surprise in Section 16.2: two utterly different sets carry the
SAME group structure. The map f(x) = [[1, x], [0, 1]] turns addition
of reals into multiplication of matrices, because

    [[1,a],[0,1]] [[1,b],[0,1]] = [[1, a+b],[0,1]].

We check the homomorphism law f(x + y) = f(x) f(y) on random reals,
and confirm f is a bijection by inverting it (read off the top-right
entry). Geometrically each matrix is a shear; composing shears adds
their magnitudes.
"""
import numpy as np

rng = np.random.default_rng(16)


def f(x):
    return np.array([[1.0, x], [0.0, 1.0]])


def f_inverse(M):
    return M[0, 1]


for _ in range(10000):
    a, b = rng.uniform(-50, 50, size=2)
    # Homomorphism: addition in R  ->  multiplication in the matrix group.
    assert np.allclose(f(a + b), f(a) @ f(b))
    # Bijection: recover the real number from the matrix.
    assert np.isclose(f_inverse(f(a)), a)

print("f(x) = [[1,x],[0,1]] satisfies f(a+b) = f(a) f(b) for all tested a,b.")
print("f is invertible (top-right entry), so (R,+) and the shear group")
print("are isomorphic: same structure, different clothing.")
