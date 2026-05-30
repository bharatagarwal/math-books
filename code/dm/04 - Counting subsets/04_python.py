# uv run --with sympy python
# Distributing presents (section 4.4) and anagrams (section 4.5):
# both are counted by the multinomial  n! / (n_1! n_2! ... n_k!).
# We verify the closed form two ways:
#   1) the book's "select for child 1, then child 2, ..." product
#      of binomials (ex. 4.15)
#   2) direct brute-force enumeration of distinct anagrams for words.
# Reproduces: STATUS / LETTER -> 6!/(2!2!) = 180 (ex. 4.21), and
# COMBINATORICS (ex. 4.18).

from collections import Counter
from itertools import permutations

import sympy as sp


def multinomial(counts):
    # n! / (n_1! ... n_k!)
    n = sum(counts)
    denom = 1
    for c in counts:
        denom *= sp.factorial(c)
    return sp.factorial(n) // denom


def binomial_product(counts):
    # ex. 4.15: choose n_1 of n, then n_2 of the rest, etc. -> same multinomial.
    remaining = sum(counts)
    prod = sp.Integer(1)
    for c in counts:
        prod *= sp.binomial(remaining, c)
        remaining -= c
    return prod


# (1) The two formulas agree (ex. 4.15 = section 4.4 result).
for counts in [(2, 2, 1, 1), (2, 1, 1, 1, 1), (5, 3), (2, 2, 2)]:
    assert multinomial(counts) == binomial_product(counts)
print("Multinomial == product-of-binomials for all tested splits (ex. 4.15).")

# (2) STATUS and LETTER: both 6 letters, two letters twice, two letters once.
for word in ("STATUS", "LETTER"):
    counts = list(Counter(word).values())
    m = multinomial(counts)
    print(f"{word}: letter counts {dict(Counter(word))} -> anagrams = {m}")
    assert m == sp.factorial(6) // (sp.factorial(2) * sp.factorial(2))
    assert m == 180
    # brute-force: count DISTINCT permutations of the multiset of letters
    distinct = len(set(permutations(word)))
    assert distinct == int(m), f"{word}: brute {distinct} != formula {m}"
print(
    "Brute-force distinct permutations confirm 180 for "
    "STATUS and LETTER (ex. 4.21)."
)

# (3) COMBINATORICS (ex. 4.18): 13 letters, repeats C,O,I twice each.
word = "COMBINATORICS"
counts = list(Counter(word).values())
m = multinomial(counts)
print(f"COMBINATORICS: counts {dict(Counter(word))}")
print(f"COMBINATORICS anagrams = 13!/(2!2!2!) = {m}")
assert m == sp.factorial(13) // (sp.factorial(2) ** 3)

# (4) Present-distribution example 4.16(d):
#     k=3, n=6, n1=n2=n3=2  ->  6!/(2!2!2!) = 90.
assert multinomial((2, 2, 2)) == 90
print("Present split n=6 into (2,2,2): 6!/(2!2!2!) =", multinomial((2, 2, 2)))
