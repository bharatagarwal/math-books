# uv run --with numpy python \
#   code/bradfield/08-linear-algebra-2/05_colspace_nullspace.py
#
# INTUITION DEMO (3Blue1Brown ch 7): build the column space and
# null space of a singular map and *look*. A = [[1,2],[2,4]]
# squishes the plane onto a single LINE (its column space). So:
#   - rank drops from 2 to 1 (it is "rank 1");
#   - vectors that land on the origin form a whole LINE (the
#     null space), not just the zero vector;
#   - a target b is reachable iff it sits ON that output line;
#   - when it is reachable, every null-space vector added to one
#     solution is another solution -> infinitely many.
import numpy as np

A = np.array([[1.0, 2.0], [2.0, 4.0]])
print("A =\n", A)
print(f"det(A) = {np.linalg.det(A):.1f}  (0 -> squishes the plane)")
print(f"rank(A) = {np.linalg.matrix_rank(A)}  (image is a line)\n")

# Watch where a grid of inputs lands: every output is a multiple
# of (1, 2) -- the column space really is one line.
print("inputs -> outputs (all land on the line t*(1,2)):")
for v in [(1, 0), (0, 1), (1, 1), (2, -1), (-1, 3)]:
    out = A @ np.array(v, float)
    t = out[0] / 1.0  # output = t * (1, 2)
    assert np.allclose(out, t * np.array([1.0, 2.0]))
    print(f"  {v} -> {out}  =  {t:+.0f} * (1, 2)")

# The null space: which directions get crushed to the origin?
# (1, -0.5) does, and so does every scalar multiple of it.
null_dir = np.array([2.0, -1.0])
assert np.allclose(A @ null_dir, [0.0, 0.0])
print(f"\nnull space = span of {null_dir} (A sends it to 0)")

# b = (3, 6) lies on the output line, so it is reachable.
b = np.array([3.0, 6.0])
x0 = np.array([3.0, 0.0])  # one solution: A x0 = (3, 6)
assert np.allclose(A @ x0, b)
print(f"\nb = {b} is on the line -> solvable. one x0 = {x0}")
print("add any multiple of the null direction, still a solution:")
for s in (-2.0, 0.0, 1.5):
    x = x0 + s * null_dir
    assert np.allclose(A @ x, b)
    print(f"  x0 + {s:+.1f}*null = {x}  ->  A x = {A @ x}")
print("\nso a rank-1 squish gives a 1-parameter family of solutions")
