# uv run --with sympy python code/bradfield/12-revision/05_coprime_discover.py
# CAPSTONE INTUITION (probability + number theory + counting): DISCOVER that two
# random integers are coprime with probability ~ 6/pi^2, and see WHY, prime by
# prime. No formula assumed -- we grow N, watch the empirical fraction settle,
# then build the Euler product that explains it.
from math import gcd, pi
from sympy import primerange

# --- 1. Watch the empirical coprime fraction as the range N grows. ----------
# Pr two of {1..N} are coprime = (#coprime ordered pairs) / N^2.  We just count.
print("N      coprime-fraction   6/pi^2")
target = 6 / pi**2
for N in [10, 50, 200, 500, 1000]:
    coprime = sum(1 for a in range(1, N + 1)
                    for b in range(1, N + 1) if gcd(a, b) == 1)
    frac = coprime / (N * N)
    print(f"{N:<6} {frac:.6f}           {target:.6f}")

# --- 2. Discover the MECHANISM: prime-by-prime independence. -----------------
# A pair is coprime iff NO prime divides both. A random integer is divisible by
# prime p with prob 1/p, so both are with prob 1/p^2; "neither shares p" has
# prob (1 - 1/p^2). Treating the primes as independent and multiplying:
#     Pr[coprime] = product over primes p of (1 - 1/p^2).
# Print the partial products and watch them descend toward 6/pi^2.
print("\nEuler product (1 - 1/p^2) over the first few primes:")
prod = 1.0
for p in primerange(2, 40):
    prod *= 1 - 1 / p**2
    print(f"  up to p={p:<3} partial product = {prod:.6f}")

print(f"\nEuler product is converging to 6/pi^2 = {target:.6f}")
