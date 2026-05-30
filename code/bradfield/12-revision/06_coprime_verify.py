# uv run --with sympy python code/bradfield/12-revision/06_coprime_verify.py
# CAPSTONE VERIFICATION (probability + number theory): the coprime probability
# equals 6/pi^2 EXACTLY, via Euler's identity zeta(2) = pi^2/6. We confirm
# (a) the symbolic identity, (b) the Euler product over primes = 1/zeta(2), and
# (c) that a large empirical count matches 6/pi^2.
from math import gcd, pi
import sympy as sp

# (a) Euler's exact evaluation of zeta(2): sum_{k>=1} 1/k^2 = pi^2 / 6.
k = sp.symbols("k", positive=True, integer=True)
zeta2 = sp.summation(1 / k**2, (k, 1, sp.oo))
assert sp.simplify(zeta2 - sp.pi**2 / 6) == 0
print("zeta(2) = sum 1/k^2 =", zeta2, "= pi^2/6")

# The coprime probability is 1/zeta(2) -- the reciprocal of that sum.
target = float(1 / zeta2)               # = 6/pi^2
assert abs(target - 6 / pi**2) < 1e-12

# (b) Euler product: prod_p 1/(1 - 1/p^2) = zeta(2), so prod_p (1 - 1/p^2)
#     = 1/zeta(2). Check the partial product over many primes approaches it.
prod = 1.0
for p in sp.primerange(2, 5000):
    prod *= 1 - 1 / p**2
assert abs(prod - target) < 1e-4
print(f"prod_p (1 - 1/p^2) over primes < 5000 = {prod:.6f} ~ 6/pi^2")

# (c) Empirical: count coprime ordered pairs in {1..N}^2 and compare to 6/pi^2.
N = 1500
coprime = sum(1 for a in range(1, N + 1)
                for b in range(1, N + 1) if gcd(a, b) == 1)
frac = coprime / (N * N)
assert abs(frac - target) < 5e-3
print(f"empirical coprime fraction in 1..{N} = {frac:.6f},",
      f"6/pi^2 = {target:.6f}")
