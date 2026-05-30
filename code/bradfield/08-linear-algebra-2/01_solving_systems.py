# uv run --with numpy python \
#   code/bradfield/08-linear-algebra-2/01_solving_systems.py
#
# Ax = b through the 3Blue1Brown ch 7 lens: det != 0 gives a
# unique solution x = A^-1 b; det == 0 squishes space, so the
# answer is "none" or "infinitely many" depending on whether b
# lands in the column space. The clean test compares rank(A)
# with rank([A | b]).
import numpy as np


def classify(A, b):
    A = np.array(A, float)
    b = np.array(b, float)
    rA = np.linalg.matrix_rank(A)
    rAb = np.linalg.matrix_rank(np.column_stack([A, b]))
    n = A.shape[1]
    if rA == rAb == n:
        return "unique", np.linalg.solve(A, b)
    if rA == rAb:
        return "infinitely many", None
    return "none", None


# Case 1: invertible (det != 0), exactly one solution.
A1 = [[2.0, 1.0], [1.0, 3.0]]
b1 = [3.0, 5.0]
kind, x = classify(A1, b1)
assert kind == "unique"
assert np.allclose(np.array(A1) @ x, b1)
assert not np.isclose(np.linalg.det(A1), 0.0)
print(f"det != 0  -> {kind}: x = {x}")

# Case 2: singular, b NOT in the column space -> no solution.
A2 = [[1.0, 2.0], [2.0, 4.0]]  # second row = 2 x first
b2 = [1.0, 3.0]                # 3 != 2*1, off the line
kind2, _ = classify(A2, b2)
assert kind2 == "none"
assert np.isclose(np.linalg.det(A2), 0.0)
print(f"det == 0, b off column space -> {kind2}")

# Case 3: singular, b IN the column space -> infinitely many.
b3 = [1.0, 2.0]               # exactly 2x the first row
kind3, _ = classify(A2, b3)
assert kind3 == "infinitely many"
print(f"det == 0, b in column space  -> {kind3}")

print("trichotomy verified: unique / none / infinitely many")
