# uv run --with numpy python code/bradfield/02-probability/03_expectation.py
# Expectation and the killer technique: LINEARITY of expectation.
from itertools import permutations
from fractions import Fraction
import numpy as np

# E[X] = sum over outcomes of value * probability. For a fair die, E = 3.5.
die = [Fraction(1, 6) for _ in range(6)]  # P(X=v) = 1/6 for each face v
EX = sum(v * p for v, p in zip(range(1, 7), die))
assert EX == Fraction(7, 2)

# Linearity: E[X+Y] = E[X] + E[Y] -- ALWAYS, even when X, Y are dependent.
# Showpiece: expected number of fixed points of a random permutation of n.
# Let X_i = 1 if position i is fixed. P(X_i=1) = 1/n, so E[fixed] = n*(1/n) = 1,
# for EVERY n. The indicators are dependent; linearity does not care.
def avg_fixed_points_exact(n):
    total = sum(sum(1 for i, v in enumerate(p) if i == v)
                for p in permutations(range(n)))
    from math import factorial
    return Fraction(total, factorial(n))

for n in range(1, 8):
    assert avg_fixed_points_exact(n) == 1

# Simulate for a larger n where enumeration is hopeless.
rng = np.random.default_rng(2)
n, trials = 50, 100_000
fixed = np.array([
    int(np.sum(rng.permutation(n) == np.arange(n))) for _ in range(trials)
])
assert abs(fixed.mean() - 1.0) < 0.05

print("E[die] =", EX)
print("E[fixed points] = 1 for n = 1..7 (exact);",
      "n=50 simulated =", round(fixed.mean(), 3))
