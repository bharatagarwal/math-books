# uv run python
# Theorem 4.2: the number of k-subsets of an n-set is C(n,k) = n!/(k!(n-k)!).
# We *enumerate* every k-subset with itertools.combinations and confirm
# the count equals the closed form, using only the standard library.
# Reproduces the book's named instances: handshakes C(7,2) and lottery C(90,5).

from itertools import combinations
from math import comb, factorial


def closed_form(n, k):
    # n!/(k!(n-k)!) written exactly as in Theorem 4.2.
    return factorial(n) // (factorial(k) * factorial(n - k))


# Brute-force enumeration vs. formula for small n (Theorem 4.2).
print("Enumerated k-subset counts vs n!/(k!(n-k)!):")
for n in range(0, 7):
    for k in range(0, n + 1):
        enumerated = sum(1 for _ in combinations(range(n), k))
        formula = closed_form(n, k)
        assert enumerated == formula == comb(n, k)
    row = [closed_form(n, k) for k in range(n + 1)]
    print(f"  n={n}: {row}")

# Book's named examples.
print("Handshakes among 7 people  C(7,2) =", closed_form(7, 2))   # 21
print("Lottery tickets            C(90,5) =", closed_form(90, 5))  # 43949268

# Spot-check the enumeration literally for the handshake example:
people = ["A", "B", "C", "D", "E", "F", "G"]
handshakes = list(combinations(people, 2))
print("Enumerated handshakes:", len(handshakes), "==", closed_form(7, 2))
assert len(handshakes) == 21

# Symmetry  C(n,k) = C(n, n-k)  (exercise 4.9).
for n in range(0, 11):
    for k in range(0, n + 1):
        assert comb(n, k) == comb(n, n - k)
print("Symmetry C(n,k)=C(n,n-k) verified for n<=10.")

print("Theorem 4.2 verified by enumeration.")
