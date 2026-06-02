# uv run python "code/pim/03 - Sets/06_induction_step.py"
# Make the inductive step concrete: split (X choose 2) for
# X = {1,...,n+1} into pairs entirely inside Y = {1,...,n} and
# pairs that contain the new element n+1. The proof claims these
# two parts are disjoint, cover everything, and have sizes
# |(Y choose 2)| = (n choose 2) and n respectively.
from itertools import combinations


def choose_two(X):
    return set(frozenset(p) for p in combinations(X, 2))


for n in range(2, 10):
    X = list(range(1, n + 2))          # {1, ..., n+1}
    new = n + 1
    Y = list(range(1, n + 1))          # {1, ..., n}

    all_pairs = choose_two(X)
    both_in_Y = {p for p in all_pairs if new not in p}
    has_new = {p for p in all_pairs if new in p}

    # Disjoint and covering: a genuine partition.
    assert both_in_Y | has_new == all_pairs
    assert both_in_Y & has_new == set()

    # The two part sizes the proof asserts.
    assert both_in_Y == choose_two(Y)
    assert len(both_in_Y) == n * (n - 1) // 2     # = (n choose 2)
    assert len(has_new) == n                       # pair n+1 with any y

    # So the total telescopes to 1 + 2 + ... + n.
    assert len(all_pairs) == sum(range(1, n + 1))
    print(f"n={n}: ({n+1} choose 2) = {len(all_pairs):2d}"
          f" = (n choose 2)={len(both_in_Y):2d} + n={len(has_new)}")

print("inductive step verified: the partition bookkeeping holds")
