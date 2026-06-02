# uv run python "code/pim/03 - Sets/09_fano.py"
# Exercise 4.10: an explicit Steiner (7, 3, 2)-system -- the Fano
# plane. A family of 3-element subsets ("lines") of {1,...,7} such
# that every 2-element subset (pair) lies in EXACTLY one line.
from itertools import combinations
from collections import Counter

# Seven lines of the Fano plane on points 1..7.
lines = [
    {1, 2, 3},
    {1, 4, 5},
    {1, 6, 7},
    {2, 4, 6},
    {2, 5, 7},
    {3, 4, 7},
    {3, 5, 6},
]

points = set(range(1, 8))

# Every line has size k = 3.
assert all(len(line) == 3 for line in lines)

# Count, for each pair, how many lines contain it.
pair_cover = Counter()
for line in lines:
    for pair in combinations(sorted(line), 2):
        pair_cover[pair] += 1

all_pairs = list(combinations(sorted(points), 2))
assert len(all_pairs) == 21          # (7 choose 2)

# Steiner condition: every pair is covered EXACTLY once.
for pair in all_pairs:
    assert pair_cover[pair] == 1, (pair, pair_cover[pair])

# A Steiner (7,3,2) has exactly 7 lines, each point on 3 lines.
assert len(lines) == 7
point_cover = Counter()
for line in lines:
    for p in line:
        point_cover[p] += 1
assert all(point_cover[p] == 3 for p in points)

print("Fano plane verified as a Steiner (7, 3, 2)-system:")
print("  7 lines, every one of the 21 pairs covered exactly once,")
print("  every point lying on exactly 3 lines")
