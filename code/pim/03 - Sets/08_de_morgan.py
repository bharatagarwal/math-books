# uv run python "code/pim/03 - Sets/08_de_morgan.py"
# Exercise 4.2: De Morgan's laws for sets, and the matching boolean
# identities. Set version checked over all subsets of a universe;
# boolean version checked over all truth assignments. They are the
# same statement via the subset-vs-indicator bijection of Ex 4.1.
from itertools import combinations, product

X = set(range(6))   # the universe


def subsets(U):
    U = list(U)
    for r in range(len(U) + 1):
        for c in combinations(U, r):
            yield set(c)


def complement(S):
    return X - S


pairs_checked = 0
for A in subsets(X):
    for B in subsets(X):
        # (A cap B)^C = A^C cup B^C
        assert complement(A & B) == complement(A) | complement(B)
        # (A cup B)^C = A^C cap B^C
        assert complement(A | B) == complement(A) & complement(B)
        pairs_checked += 1
print(f"set De Morgan verified on {pairs_checked} (A, B) pairs")

# Boolean version: not (a and b) == (not a) or (not b), etc.
for a, b in product([False, True], repeat=2):
    assert (not (a and b)) == ((not a) or (not b))
    assert (not (a or b)) == ((not a) and (not b))
print("boolean De Morgan verified on all 4 truth assignments")
print("same law, two costumes: complement <-> negation")
