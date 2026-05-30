# uv run --with sympy python
# Fermat's Little Theorem (section 8.5, Thm 8.6) and its failure as a
# primality test (8.7).  Reproduces every concrete number the book gives:
#   primes p divide a^p - a;
#   341 = 11*31 is the smallest base-2 Fermat pseudoprime
#   (341 | 2^340 - 1) yet composite;  base 3 already exposes 341;
#   561 = 3*11*17 is a Carmichael number: 561 | a^561 - a for EVERY a.
from sympy import isprime, factorint, primerange


def factor_string(n):
    """Render n as p1*p2*... with each prime repeated to its exponent."""
    f = factorint(n)
    return "*".join(str(p) for p in sorted(f) for _ in range(f[p]))


# --- Fermat's Little Theorem: p | a^p - a for every prime p,
#     every integer a (Thm 8.6) ---
ok = all((a**p - a) % p == 0
         for p in primerange(2, 50)
         for a in range(0, 30))
print("FLT  p | a^p - a  for all primes p<50, a in 0..29:", ok)
assert ok

# --- The book's failed-divisor table (section 8.7): odd composites
#     that are NOT base-2 pseudoprimes, n does NOT divide 2^(n-1) - 1.
for n, val in [(9, 255), (15, 16383), (21, 1048575), (25, 16777215)]:
    assert 2**(n - 1) - 1 == val            # the exact value the book prints
    assert (2**(n - 1) - 1) % n != 0        # n does not divide it
    print(f"2^{n-1}-1 = {val:,};"
          f"  {n} does NOT divide it (correctly flags composite)")

# --- 341 = 11*31: the smallest base-2 Fermat pseudoprime ---
print("341 =", factor_string(341))
print("341 prime?", isprime(341),
      " but 341 | 2^340 - 1 ?", (2**340 - 1) % 341 == 0)
# composite yet passes the base-2 test
assert not isprime(341) and (2**340 - 1) % 341 == 0
# the book's hand argument: 2^10 - 1 = 1023 = 3 * 11 * 31, so 341 | 2^10 - 1
assert (2**10 - 1) % 341 == 0
# base 3 rules out 341 (book: "already the first of these rules out
# the fake prime 341")
print("but base 3:  341 | 3^340 - 1 ?", (3**340 - 1) % 341 == 0,
      "-> exposed as composite")
assert (3**340 - 1) % 341 != 0

# --- 561 = 3*11*17: a Carmichael number.  561 | a^561 - a for EVERY a
#     (no base escapes). ---
print("561 =", factor_string(561), " prime?", isprime(561))
carmichael = all((pow(a, 561, 561) - a) % 561 == 0 for a in range(0, 561))
print("561 | a^561 - a for ALL a in 0..560 :", carmichael,
      "  <- Carmichael (ex 8.30)")
assert carmichael and not isprime(561)

# count base-2 Fermat pseudoprimes below 10000
# (book: "only 22 of them between 1 and 10,000")
psp = [n for n in range(3, 10000, 2)
       if not isprime(n) and (2**(n - 1) - 1) % n == 0]
print(f"base-2 Fermat pseudoprimes < 10000: {len(psp)} of them"
      f"  (book says 22)")
print("first few:", psp[:6])
assert len(psp) == 22
