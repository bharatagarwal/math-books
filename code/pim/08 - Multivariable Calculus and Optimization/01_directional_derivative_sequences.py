# uv run --with numpy python "code/pim/08 - Multivariable Calculus and Optimization/01_directional_derivative_sequences.py"
#
# Kun's well-definition counterexample: the naive vector derivative
#   lim (f(x_n) - f(c)) / ||x_n - c||
# gives DIFFERENT answers along different sequences converging to c,
# so it is not well-defined.  f(x1, x2) = -x2^2, c = (1, 1).
import numpy as np


def f(x):
    return -x[1] ** 2


c = np.array([1.0, 1.0])

# Sequence x_n  = (1 + 1/n, 1): approaches along x1 (f flat there).
# Sequence x_n' = (1, 1 + 1/n): approaches along x2 (f quadratic).
def naive_quotient(seq_fn, n):
    x = seq_fn(n)
    return (f(x) - f(c)) / np.linalg.norm(x - c)


seq_along_x1 = lambda n: np.array([1.0 + 1.0 / n, 1.0])
seq_along_x2 = lambda n: np.array([1.0, 1.0 + 1.0 / n])

ns = [10, 100, 1000, 10000, 100000]
print("n        along x1      along x2")
for n in ns:
    q1 = naive_quotient(seq_along_x1, n)
    q2 = naive_quotient(seq_along_x2, n)
    print(f"{n:<8} {q1:>10.5f}   {q2:>10.5f}")

limit_x1 = naive_quotient(seq_along_x1, 10 ** 7)
limit_x2 = naive_quotient(seq_along_x2, 10 ** 7)

# The x1 sequence limits to 0 (f does not change), the x2 sequence to -2.
assert abs(limit_x1 - 0.0) < 1e-4, limit_x1
assert abs(limit_x2 - (-2.0)) < 1e-3, limit_x2
assert abs(limit_x1 - limit_x2) > 1.0  # genuinely different => ill-defined

print()
print(f"limit along x1 = {limit_x1:.5f}  (Kun's  0)")
print(f"limit along x2 = {limit_x2:.5f}  (Kun's -2)")
print("Different limits => the naive vector derivative is not well-defined.")
