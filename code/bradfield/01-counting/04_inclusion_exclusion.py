# uv run python code/bradfield/01-counting/04_inclusion_exclusion.py
# Inclusion-exclusion, checked against a literal count over the universe.
U = set(range(1, 1001))  # {1, ..., 1000}

A = {n for n in U if n % 2 == 0}   # divisible by 2
B = {n for n in U if n % 3 == 0}   # divisible by 3
C = {n for n in U if n % 5 == 0}   # divisible by 5

# Ground truth: size of the union, computed directly.
truth = len(A | B | C)

# Inclusion-exclusion for three sets.
ie = (
    len(A) + len(B) + len(C)
    - len(A & B) - len(A & C) - len(B & C)
    + len(A & B & C)
)
assert ie == truth

# A classic use: count integers in 1..1000 divisible by NONE of 2,3,5.
none = len(U) - truth
assert none == len(U - (A | B | C))

print("|A u B u C| =", truth, "(inclusion-exclusion agrees)")
print("divisible by none of 2,3,5:", none)
