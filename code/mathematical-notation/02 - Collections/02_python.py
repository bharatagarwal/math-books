# uv run python
# Set-builder notation → Python set comprehension.
# Math: {x ∈ Z : 1 ≤ x ≤ 100 and x divisible by 5}
# Python: {x for x in range(1, 101) if x % 5 == 0}

S = {x for x in range(1, 101) if x % 5 == 0}
print(f"multiples of 5 in [1,100]: {sorted(S)}")
print(f"|S| = {len(S)}")

# Power set: all subsets of {1, 2, 3}
from itertools import combinations
A = {1, 2, 3}
power_set = set()
for r in range(len(A) + 1):
    for subset in combinations(A, r):
        power_set.add(frozenset(subset))
print(f"P({{1,2,3}}) has {len(power_set)} elements = 2^{len(A)}")
# |S| = 20
# P({1,2,3}) has 8 elements = 2^3
