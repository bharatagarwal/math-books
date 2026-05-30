# uv run python code/bradfield/10-number-theory/07_fermat_table.py
# INTUITION (LL ch 8, sec 8.5 & 8.7): print the table of a^(p-1) mod p and
# SEE Fermat's Little Theorem -- for a PRIME p, every a in 1..p-1 gives 1.
# For a composite n the row of 1s breaks (some a coprime to n is not 1) --
# UNLESS n is a pseudoprime.  Then watch the same idea fail as a primality
# test on the pseudoprime 341 and the Carmichael number 561.
import math


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))


def row(n):
    # a^(n-1) mod n for the a in 1..n-1 that are coprime to n (the only ones
    # FLT speaks about).  Theorem 8.6: prime p => a^(p-1) = 1 for all such a.
    coprime = [a for a in range(1, n) if math.gcd(a, n) == 1]
    return coprime, [pow(a, n - 1, n) for a in coprime]


print("a^(n-1) mod n over a coprime to n   (FLT: a PRIME gives an all-1 row)")
for n in range(3, 14):
    coprime, vals = row(n)
    allone = all(v == 1 for v in vals)
    # Forward direction of Fermat (Theorem 8.6): prime => the row is all 1s.
    if is_prime(n):
        assert allone
    tag = "PRIME, all 1s" if is_prime(n) else (
        "composite, row breaks" if not allone else "composite (sneaky 1s)")
    print(f"  n={n:2d} [{tag:>22}]  a={coprime} -> {vals}")

# LL sec 8.7: the divisibility table n | 2^(n-1) - 1 for small odd composites.
# None of these hold -- so the Fermat test correctly rejects them.
print()
print("n | 2^(n-1) - 1 ?   (the book's table -- none divide, all composite)")
for n, val in [(9, 2**8 - 1), (15, 2**14 - 1),
               (21, 2**20 - 1), (25, 2**24 - 1)]:
    divides = (val % n == 0)
    assert not divides
    print(f"  {n}: 2^{n-1}-1 = {val:>9}   divisible by {n}? {divides}")

# The catch (LL sec 8.7): 341 = 11*31 is composite yet PASSES the base-2 test.
print()
print("the false positive: 341 = 11 * 31")
print("  341 prime?            ", is_prime(341))
print("  341 | 2^340 - 1 ?     ", pow(2, 340, 341) == 1, "(base 2 fooled)")
print("  but base 3 exposes it: 3^340 mod 341 =", pow(3, 340, 341),
      "!= 1" if pow(3, 340, 341) != 1 else "")
assert not is_prime(341)
assert pow(2, 340, 341) == 1 and pow(3, 340, 341) != 1

# Worse: 561 = 3*11*17 is a Carmichael number -- it passes for EVERY base.
print()
print("the Carmichael number: 561 = 3 * 11 * 17 passes for every base a")
carmichael = all(pow(a, 561, 561) == a % 561 for a in range(561))
print("  561 | a^561 - a for ALL a in 0..560 ?", carmichael)
assert carmichael and not is_prime(561)
print("  this is why a Fermat-only test is not a real primality test")
