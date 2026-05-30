# uv run python code/bradfield/01-counting/06_discover_doubling.py
# INTUITION (not verification): don't assume 2^n -- DISCOVER it. Build the actual
# powerset for n = 0,1,2,3,... , watch the count, and notice it doubles. Then see
# *why*: adding one new element splits into "old subsets without it" + "the same
# subsets with it added" -- two copies, hence x2 each step.
from itertools import chain, combinations

def powerset(items):
    return [set(c) for r in range(len(items) + 1)
            for c in combinations(items, r)]

print("n | #subsets | ratio to previous row")
prev = None
for n in range(6):
    ps = powerset(range(n))
    count = len(ps)
    ratio = "-" if prev is None else f"x{count // prev}"
    print(f"{n} | {count:>8} | {ratio}")
    prev = count

# Now SEE the doubling mechanism for the step n=2 -> n=3.
without_c = powerset(["a", "b"])                 # subsets of {a,b}
with_c = [s | {"c"} for s in without_c]          # each, plus the new element c
print("\nsubsets of {a,b}        :", [sorted(s) for s in without_c])
print("...each with 'c' added  :", [sorted(s) for s in with_c])
print("together = subsets of {a,b,c}: 4 + 4 = 8  -> the count doubled")
