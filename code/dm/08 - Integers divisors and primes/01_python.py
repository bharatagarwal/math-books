# uv run --with sympy python
# Unique factorization (Theorem 8.1) and the prime-counting
# estimates of section 8.4.  Reproduces the book's worked numbers:
#   300 = 2^2 * 3 * 5^2,  18 = 2 * 3^3,
#   gcd via shared prime powers = 2*3 = 6,
#   the "1 in 460" density of 200-digit primes,
#   and "1 in 2.3k" for k-digit numbers.
from math import gcd, log, prod
from sympy import factorint, primepi

# --- Unique factorization: every n>1 factors into primes,
#     uniquely (Thm 8.1) ---
for n in (300, 18):
    f = factorint(n)                      # {prime: exponent}
    # check the factorization actually multiplies back to n
    assert prod(p**e for p, e in f.items()) == n
    print(f"{n} = " + " * ".join(f"{p}^{e}" for p, e in f.items()))

f300, f18 = factorint(300), factorint(18)
print("factorint(300) =", f300, " factorint(18) =", f18)

# gcd by "common primes, smaller exponent, take the product"
# (the book's prime-power recipe)
common = set(f300) & set(f18)
gcd_via_primes = prod(p ** min(f300[p], f18[p]) for p in common)
print("gcd(300,18) via shared prime powers =", gcd_via_primes,
      "  (matches math.gcd:", gcd(300, 18) == gcd_via_primes, ")")
assert gcd_via_primes == 6 == gcd(300, 18)

# --- sqrt(2) irrational, mechanized (Thm 8.2): 2 appears an EVEN
#     number of times in any square's factorization, so 2*b^2 = a^2
#     is impossible. ---
def power_of_2_in(n):
    return factorint(n).get(2, 0)
for b in range(1, 50):
    a2 = 2 * b * b
    # exponent of 2 in 2*b^2 is odd; in any perfect square a^2 it is
    # even -> the two can never be equal
    assert power_of_2_in(a2) % 2 == 1, b
print("checked b=1..49: exponent of 2 in 2*b^2 is always ODD"
      " -> 2*b^2 is never a square")

# --- Prime Number Theorem density estimates (section 8.4) ---
# "among integers with 200 digits, one in every ~460 is a prime"
ln10 = log(10)
primes_200_digit = 10**200 / (200 * ln10) - 10**199 / (199 * ln10)
ints_200_digit = 9 * 10**199
print(f"approx # of 200-digit primes ~ {primes_200_digit:.3e}"
      f"  (book: ~1.95e197)")
print(f"density 1 in {ints_200_digit / primes_200_digit:.0f}"
      f"  (book: ~460)")

# the general "one in about 2.3k" rule for k-digit numbers
# (exercise 8.13): ln(10) ~ 2.303
print(f"ln(10) = {ln10:.4f}"
      f"  ->  one k-digit number in about 2.3k is prime")

# exact primepi cross-check of the asymptotic on a small range
print("pi(1000) exact =", primepi(1000),
      "  n/ln n approx =", round(1000 / log(1000)))
