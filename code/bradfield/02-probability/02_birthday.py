# uv run --with numpy python code/bradfield/02-probability/02_birthday.py
# The birthday "paradox": P(some shared birthday among k people).
from fractions import Fraction
import numpy as np

# Exact: complement of "all distinct". All distinct has probability
# 365/365 * 364/365 * ... * (365-k+1)/365.
def p_shared(k, days=365):
    distinct = Fraction(1)
    for i in range(k):
        distinct *= Fraction(days - i, days)
    return 1 - distinct

p23 = p_shared(23)
assert p23 > Fraction(1, 2)          # 23 people already tips past 50%
assert p_shared(22) < Fraction(1, 2)  # ...and 22 does not

# Simulation agrees.
rng = np.random.default_rng(1)
trials, k = 200_000, 23
bdays = rng.integers(0, 365, size=(trials, k))
# A collision exists iff sorting reveals two equal adjacent values.
bdays.sort(axis=1)
has_dup = (np.diff(bdays, axis=1) == 0).any(axis=1)
sim = has_dup.mean()
assert abs(sim - float(p23)) < 0.01

print("P(shared birthday, k=23) exact =", round(float(p23), 4),
      " simulated =", round(float(sim), 4))
