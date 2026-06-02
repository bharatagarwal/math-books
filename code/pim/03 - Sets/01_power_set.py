# uv run python "code/pim/03 - Sets/01_power_set.py"
# Build the power set 2^S explicitly and check |2^S| = 2^|S|.
# The construction IS the proof: each subset corresponds to one
# bitmask over the elements, so subsets biject with binary strings.
from itertools import product


def power_set(S):
    """All subsets of S, as a list of frozensets."""
    elems = list(S)
    subsets = []
    for bits in product([0, 1], repeat=len(elems)):
        chosen = frozenset(e for e, b in zip(elems, bits) if b)
        subsets.append(chosen)
    return subsets


for n in range(0, 8):
    S = set(range(n))
    P = power_set(S)
    # No duplicate subsets: the bitmask map is injective.
    assert len(set(P)) == len(P)
    # Cardinality identity |2^S| = 2^|S|.
    assert len(P) == 2 ** n
    print(f"|S| = {n}:  |2^S| = {len(P)} = 2^{n}")

# The empty set has exactly one subset: itself.
assert power_set(set()) == [frozenset()]

# Spell out the bijection 2^A <-> functions A -> {0,1} for a tiny A.
A = ["x", "y"]
for subset in power_set(A):
    indicator = {a: (1 if a in subset else 0) for a in A}
    # Recover the subset as the preimage of 1, per Exercise 4.1.
    recovered = frozenset(a for a in A if indicator[a] == 1)
    assert recovered == subset
print("subset <-> indicator function bijection holds for A =", A)
