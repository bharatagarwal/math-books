# cd to repo root, then:
# uv run --with sympy python \
#         code/bradfield/10-number-theory/05_factor_explore.py
# INTUITION (LL ch 8, Thm 8.1): discover primes with the sieve of
# Eratosthenes, watch unique factorization appear, then rebuild gcd from
# the shared prime powers -- the "common primes, smaller exponent" recipe.
from collections import Counter
import sympy as sp


def sieve(limit):
    # Eratosthenes: cross out multiples of each survivor; what's left is prime.
    is_p = [False, False] + [True] * (limit - 1)
    for p in range(2, int(limit**0.5) + 1):
        if is_p[p]:
            for m in range(p * p, limit + 1, p):
                is_p[m] = False
    return [n for n in range(2, limit + 1) if is_p[n]]


primes = sieve(50)
print("sieve discovers the primes up to 50:")
print(" ", primes)

# Build the factorization of every n in 2..30 and LOOK at it: each n is a
# product of primes, in exactly one way (up to order) -- Theorem 8.1.
print()
print("every integer = product of primes, uniquely (Theorem 8.1):")
for n in range(2, 31):
    f = sp.factorint(n)                       # {prime: exponent}
    pieces = " * ".join(f"{p}^{e}" for p, e in f.items())
    # rebuild from the factorization to confirm it really reconstructs n
    rebuilt = sp.prod([p**e for p, e in f.items()])
    assert rebuilt == n
    print(f"  {n:2d} = {pieces}")

# The book's gcd recipe (LL 8.6): share the common primes, take the SMALLER
# exponent of each, multiply.  300 = 2^2 * 3 * 5^2, 18 = 2 * 3^2.
fa, fb = Counter(sp.factorint(300)), Counter(sp.factorint(18))
shared = {p: min(fa[p], fb[p]) for p in fa.keys() & fb.keys()}
g = 1
for p, e in shared.items():
    g *= p**e
print()
print("300 =", dict(sp.factorint(300)), "  18 =", dict(sp.factorint(18)))
print("gcd via shared primes, smaller exponent =", g)
assert g == sp.gcd(300, 18) == 6

# Same recipe gives lcm by taking the LARGER exponent (LL exercise 8.21),
# and the two satisfy gcd * lcm = a*b (LL exercise 8.23).
biggest = {p: max(fa[p], fb[p]) for p in fa.keys() | fb.keys()}
l = 1
for p, e in biggest.items():
    l *= p**e
print("lcm via shared primes, larger exponent  =", l)
assert g * l == 300 * 18
print("check: gcd * lcm =", g * l, "= 300 * 18 =", 300 * 18)
