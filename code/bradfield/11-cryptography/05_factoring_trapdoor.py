# uv run --with sympy python \
#  code/bradfield/11-cryptography/05_factoring_trapdoor.py
# (single command; line wrapped only to fit the 80-char reader column)
"""The trapdoor: multiply-forward is cheap, factor-back blows up.

Intuition demo (LL ch 15-16). RSA is safe because computing
n = p*q is trivial but recovering p, q from n is not. We DISCOVER
the asymmetry by timing trial-division factoring as n grows, and
we show that the eavesdropper's only route to phi(n) -- and thus
to the private exponent d -- runs through that factorization.
"""
import time
from math import gcd, isqrt
from sympy import nextprime


def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


def modinv(a, mod):
    g, x, _ = egcd(a, mod)
    assert g == 1
    return x % mod


def factor(n):
    """Trial division: the naive attack on RSA."""
    for f in range(2, isqrt(n) + 1):
        if n % f == 0:
            return f, n // f
    return n, 1


# Forward direction is instant; backward grows with the size of n.
print("bits  n                     factor-time(s)")
for k in range(6, 13, 2):
    p = nextprime(2 ** k)
    q = nextprime(p)              # two nearby primes of ~k bits
    n = p * q
    t0 = time.perf_counter()
    f1, f2 = factor(n)
    dt = time.perf_counter() - t0
    assert {f1, f2} == {p, q}     # factoring did recover p, q
    print(f"{n.bit_length():>4}  {n:<20}  {dt:.6f}")
print("multiplying p*q is one step; factoring back scales with"
      " sqrt(n) here -- the gap is the trapdoor")

# The eavesdropper's bind: with only (n, e) you cannot get d
# without phi(n), and phi(n) = (p-1)(q-1) needs the factorization.
p, q = nextprime(200), nextprime(300)
n = p * q
phi = (p - 1) * (q - 1)
e = next(x for x in range(3, phi, 2) if gcd(x, phi) == 1)
d = modinv(e, phi)
# Attacker factors n (feasible only because it is tiny) ...
ap, aq = factor(n)
attacker_phi = (ap - 1) * (aq - 1)
attacker_d = modinv(e, attacker_phi)
assert attacker_d == d
print(f"\nrecovered d={d} ONLY by factoring n={n} into"
      f" {ap}*{aq}; with large primes this step is infeasible")
assert gcd(e, phi) == 1
