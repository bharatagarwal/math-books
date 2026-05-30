# uv run --with numpy python code/bradfield/02-probability/01_sample_spaces.py
# Uniform probability is just counting: P(event) = |event| / |sample space|.
from itertools import product
from fractions import Fraction
import numpy as np

# Sample space: two fair six-sided dice. 36 equally likely outcomes.
omega = list(product(range(1, 7), repeat=6 // 3))  # repeat=2
assert len(omega) == 36

# Exact distribution of the sum, by counting outcomes (Fraction = no rounding).
from collections import Counter
counts = Counter(a + b for a, b in omega)
exact = {s: Fraction(c, 36) for s, c in counts.items()}
assert exact[7] == Fraction(6, 36) == Fraction(1, 6)   # 7 is the modal sum
assert sum(exact.values()) == 1                         # it's a distribution

# Monte Carlo should converge to the exact probabilities (law of large numbers).
rng = np.random.default_rng(0)
rolls = rng.integers(1, 7, size=(2, 1_000_000))
sums = rolls.sum(axis=0)
approx7 = np.mean(sums == 7)
assert abs(approx7 - 1 / 6) < 0.01

print("P(sum=7) exact =", exact[7], "~", round(float(exact[7]), 4),
      " simulated =", round(float(approx7), 4))
