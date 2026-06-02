# uv run python "code/pim/03 - Sets/04_choose_two.py"
# The picture proof of Figure 4.4: |(X choose 2)| = 1 + 2 + ... + (n-1)
# when |X| = n. We enumerate the unordered pairs directly (the set
# (X choose 2)) and compare its size to the triangular-number sum.
from itertools import combinations


def choose_two(X):
    """The set { {x, y} : x, y in X, x != y } as frozensets."""
    return [frozenset(pair) for pair in combinations(X, 2)]


def triangular(n):
    """1 + 2 + ... + (n-1), the count of balls in Figure 4.4."""
    return sum(range(1, n))


for n in range(0, 12):
    X = list(range(n))
    pairs = choose_two(X)
    # Unordered + distinct: no pair repeats, none is a singleton.
    assert all(len(p) == 2 for p in pairs)
    assert len(set(pairs)) == len(pairs)
    # The bijection's payoff: the two counts agree.
    assert len(pairs) == triangular(n)
    # And both equal the standard binomial n(n-1)/2.
    assert len(pairs) == n * (n - 1) // 2
    print(f"n = {n:2d}:  |(X choose 2)| = {len(pairs):2d}"
          f"  = 1+...+{n - 1} = {triangular(n)}")

print("picture proof verified: choosing 2 = triangular(n-1)")
