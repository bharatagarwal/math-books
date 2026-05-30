# uv run python code/bradfield/02-probability/09_binomial_shape.py
# INTUITION (LL 7.3): the Law of Large Numbers is the Pascal Triangle in
# disguise. P(A_k) = C(n,k)/2^n is one normalized row of the triangle, so the
# distribution of the head count IS a row of Pascal. We DISCOVER its bell shape
# by printing the row as a histogram, then watch the bulk concentrate toward the
# center as n grows -- which is exactly what the LLN asserts.
from fractions import Fraction
from math import comb

print("n=20 row of Pascal, normalized -- P(k heads) = C(20,k)/2^20:\n")
n = 20
row = [Fraction(comb(n, k), 2**n) for k in range(n + 1)]
peak = max(row)
for k, p in enumerate(row):
    bar = "#" * round(float(p / peak) * 40)   # scale tallest bar to 40 cols
    print(f"k={k:>2} {bar}")

# The whole row is a probability distribution: the binomial theorem forces the
# C(n,k) to sum to 2^n, so the normalized row sums to exactly 1.
assert sum(row) == 1
# It is symmetric about the center (Pascal symmetry C(n,k)=C(n,n-k)) and peaks
# at k = n/2 = 10 (the expected number of heads).
assert row == row[::-1]
assert row.index(peak) == n // 2

# Now the LLN mechanism: as n grows, what fraction of the row's mass sits in the
# central band |k/n - 1/2| <= 0.1? The single peak P(exactly n/2) SHRINKS, yet
# the band's total mass GROWS to 1 -- mass spreads to neighbors but stays near
# the center. "Close to half" wins; "exactly half" loses.
print(f"\n{'n':>5} | P(exactly n/2) | mass in |k/n-1/2|<=0.1")
for n in [20, 200, 2000, 20000]:
    total = Fraction(comb(n, n // 2), 2**n)
    lo, hi = int(0.4 * n), int(0.6 * n)
    band = Fraction(sum(comb(n, k) for k in range(lo, hi + 1)), 2**n)
    print(f"{n:>5} | {float(total):>13.4f} | {float(band):>.4f}")

# Concretely: the peak fades below 1%, while the central band rises above 99%.
assert float(Fraction(comb(20000, 10000), 2**20000)) < 0.01
band20k = sum(comb(20000, k) for k in range(8000, 12001))
assert float(Fraction(band20k, 2**20000)) > 0.99
print("\npeak -> 0, central band -> 1: that IS the Law of Large Numbers.")
