# uv run --with numpy python
#
# Law of Large Numbers, made executable (DM section 7.3).
#
# The book's example: toss a fair coin many times. The relative frequency of
# heads (number of heads / number of tosses) should settle near p = 1/2 as the
# number of tosses n grows. Corollary 7.1 quantifies this: with probability at
# least .99 the head count among 2m tosses lies within 10*sqrt(m) of m = n/2,
# i.e. within (10/sqrt(m))-fraction of the tosses. For m = 1,000,000 the book
# notes 10*sqrt(m) = m/100, so the frequency is within 1% of 1/2.
#
# This Monte-Carlo simulation prints the relative frequency at growing n and
# shows it converging to p = 1/2, and also checks the Corollary 7.1 band
# empirically: across many independent runs of 2m tosses, the fraction landing
# inside [m-10*sqrt(m), m+10*sqrt(m)] should be >= .99 (in fact ~1).

import numpy as np

rng = np.random.default_rng(20260530)
p = 0.5  # fair coin: P(H) = P(T) = 1/2

print("Law of Large Numbers: relative frequency of heads -> p = 1/2")
print(f"{'n tosses':>12} {'heads':>12} {'freq':>10} {'|freq - 1/2|':>14}")
for n in [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]:
    heads = int(rng.binomial(n, p))  # one draw = n independent tosses
    freq = heads / n
    print(f"{n:>12} {heads:>12} {freq:>10.5f} {abs(freq - p):>14.6f}")

# Corollary 7.1 band check at m = 1,000,000 (so n = 2m, band = m +- 10*sqrt(m)).
m = 1_000_000
n = 2 * m
half_width = 10 * np.sqrt(m)        # = 10_000 = m/100  -> 1% of m
lo, hi = m - half_width, m + half_width
runs = 5_000
counts = rng.binomial(n, p, size=runs)   # head counts of `runs` experiments
inside = int(np.sum((counts >= lo) & (counts <= hi)))
print()
print(f"Corollary 7.1 check: m={m:,}, n=2m={n:,}")
print(f"  band = [m - 10*sqrt(m), m + 10*sqrt(m)] = [{lo:,.0f}, {hi:,.0f}]")
print(f"  half-width 10*sqrt(m) = {half_width:,.0f} = m/100 (1% of m): "
      f"{abs(half_width - m / 100) < 1e-6}")
print(f"  fraction of {runs} experiments inside band = {inside / runs:.4f} "
      f"(theorem guarantees >= 0.99)")
print(f"  meets >= .99 guarantee: {inside / runs >= 0.99}")
