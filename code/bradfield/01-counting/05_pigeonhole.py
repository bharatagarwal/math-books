# uv run python code/bradfield/01-counting/05_pigeonhole.py
# The pigeonhole principle: if n+1 pigeons occupy n holes, some hole has >= 2.
from itertools import combinations

# Claim (MCS-flavored): from any 6 numbers in {1,...,10}, two of them sum to 11.
# The "holes" are the pairs {1,10},{2,9},{3,8},{4,7},{5,6} -- 5 holes. Pick 6
# numbers (pigeons) and two must land in the same pair, i.e. sum to 11.
pairs = [{1, 10}, {2, 9}, {3, 8}, {4, 7}, {5, 6}]

def has_pair_summing_to_11(chosen):
    return any(p <= set(chosen) for p in pairs)

# Exhaustively verify the claim for EVERY 6-subset -- no counterexample exists.
assert all(has_pair_summing_to_11(c) for c in combinations(range(1, 11), 6))

# And it is tight: a 5-subset can avoid it (one number from each pair).
witness = (1, 2, 3, 4, 5)
assert not has_pair_summing_to_11(witness)

print("every 6-subset of {1..10} contains a pair summing to 11 (verified)")
print("5 is not enough; counterexample:", witness)
