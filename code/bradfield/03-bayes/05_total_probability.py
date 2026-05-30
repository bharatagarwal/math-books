# uv run --with numpy python code/bradfield/03-bayes/05_total_probability.py
# DISCOVER the Law of Total Probability via the MCS coin-then-dice experiment.
# Flip a fair coin: heads -> roll ONE die; tails -> roll TWO dice and sum.
# What is Pr[result == 2]? Split on the coin, weight each case. (MCS 18.5)
from fractions import Fraction
import numpy as np

# Conditional probabilities of getting a 2 in each branch.
p_two_given_heads = Fraction(1, 6)        # one die shows 2
p_two_given_tails = Fraction(1, 36)       # two dice both show 1
p_heads = Fraction(1, 2)
p_tails = Fraction(1, 2)

# Law of total probability: Pr[A] = sum over partition of Pr[A|case]Pr[case].
p_two = p_two_given_heads * p_heads + p_two_given_tails * p_tails
print("Pr[result == 2] =", p_two, "(MCS: 7/72)")
assert p_two == Fraction(7, 72)

# Now run the actual experiment a few million times and watch the long-run
# frequency converge to the formula -- the law assembled from real outcomes.
rng = np.random.default_rng(0)
N = 3_000_000
heads = rng.random(N) < 0.5
d1 = rng.integers(1, 7, size=N)
d2 = rng.integers(1, 7, size=N)
result = np.where(heads, d1, d1 + d2)
freq = (result == 2).mean()
print("simulated frequency =", round(freq, 5),
      " formula =", round(float(p_two), 5))
assert abs(freq - float(p_two)) < 0.002
