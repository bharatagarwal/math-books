# uv run --with numpy python code/bradfield/12-revision/01_coupon_collector.py
# CAPSTONE (counting + probability + expectation): the coupon collector.
# How many random draws to collect all n distinct coupon types?
import numpy as np

n = 10

# Exact answer by LINEARITY OF EXPECTATION (ch 2). Once you hold i types, the
# wait for a NEW type is geometric with success prob (n-i)/n, mean n/(n-i).
# Summing: E = n * (1/n + 1/(n-1) + ... + 1/1) = n * H_n, the harmonic number.
H_n = sum(1 / k for k in range(1, n + 1))
exact = n * H_n

# Simulate to confirm.
rng = np.random.default_rng(0)
def draws_to_complete():
    seen, draws = set(), 0
    while len(seen) < n:
        seen.add(int(rng.integers(0, n)))
        draws += 1
    return draws

sims = np.array([draws_to_complete() for _ in range(30000)])
assert abs(sims.mean() - exact) < 0.5

print(f"coupon collector, n={n}: exact n*H_n = {exact:.3f},",
      f"simulated = {sims.mean():.3f}")
