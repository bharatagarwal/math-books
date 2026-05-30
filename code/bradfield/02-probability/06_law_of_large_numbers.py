# uv run --with numpy --with sympy python \
#   code/bradfield/02-probability/06_law_of_large_numbers.py
# LL 7.3: the apparent paradox of the Law of Large Numbers, DISCOVERED by
# computing both quantities as n grows -- no proof, just watch the two numbers.
import numpy as np
import sympy as sp

# Quantity A: P(EXACTLY n/2 heads). The book says this -> 0 (like sqrt(2/(pi n))).
# Quantity B: P(fraction of heads within eps of 1/2). The LLN says this -> 1.
# The resolution: "exactly half" is one outcome and fades; "close to half"
# captures a widening band of outcomes and grows to certainty.
eps = 0.05
print(f"{'n':>6} | P(exactly n/2) | P(|frac-1/2| <= {eps})")
for n in [10, 100, 1000, 10000]:
    exact_half = sp.Rational(sp.binomial(n, n // 2), 2**n)
    lo, hi = (0.5 - eps) * n, (0.5 + eps) * n
    band = sp.Rational(
        sum(sp.binomial(n, k) for k in range(int(np.ceil(lo)), int(hi) + 1)),
        2**n,
    )
    print(f"{n:>6} | {float(exact_half):>13.4f} | {float(band):>.4f}")

# So the two limits really do head in opposite directions:
assert float(sp.Rational(sp.binomial(10000, 5000), 2**10000)) < 0.01   # A -> 0
band_big = sum(sp.binomial(10000, k)
               for k in range(int(0.45 * 10000), int(0.55 * 10000) + 1))
assert float(sp.Rational(band_big, 2**10000)) > 0.99                    # B -> 1

# And a direct simulation: the running fraction of heads hugs 1/2 as n grows.
rng = np.random.default_rng(0)
flips = rng.integers(0, 2, size=100000)
frac = np.cumsum(flips) / np.arange(1, flips.size + 1)
assert abs(frac[-1] - 0.5) < 0.01
print("\nsimulated fraction of heads after 100k flips:", round(float(frac[-1]), 4))
