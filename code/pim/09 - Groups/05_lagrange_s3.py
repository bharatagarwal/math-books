# uv run python "code/pim/09 - Groups/05_lagrange_s3.py"
"""The symmetric group S_3, its Cayley table, and Lagrange's theorem.

Kun calls the symmetric group "really the permutation group": all
bijections of a fixed set. We build S_3 = all permutations of {0,1,2}
under composition, print its 6x6 Cayley table, then verify the result
of Exercise 16.7 -- Lagrange's theorem: the order of every subgroup
divides the order of the group. We do it by brute force, enumerating
every subset closed under composition and inverses.
"""
from itertools import permutations, combinations

S3 = list(permutations(range(3)))      # 6 permutations as tuples


def compose(f, g):
    return tuple(f[g[i]] for i in range(3))


identity = (0, 1, 2)
labels = {p: name for p, name in zip(
    [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (2, 1, 0), (1, 0, 2)],
    ["e", "r", "r2", "s", "rs", "r2s"])}

# Cayley table: row . column, with row applied second.
order = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (2, 1, 0), (1, 0, 2)]
header = "      " + " ".join(f"{labels[c]:>4}" for c in order)
print("Cayley table of S_3 (row composed with column):")
print(header)
for a in order:
    cells = " ".join(f"{labels[compose(a, b)]:>4}" for b in order)
    print(f"{labels[a]:>4} | {cells}")


def is_subgroup(H):
    Hs = set(H)
    if identity not in Hs:
        return False
    for a in Hs:
        for b in Hs:
            if compose(a, b) not in Hs:
                return False
    return True


# Enumerate every subset of S_3 that forms a subgroup.
subgroups = []
for size in range(1, len(S3) + 1):
    for sub in combinations(S3, size):
        if is_subgroup(sub):
            subgroups.append(sub)

print(f"\n|S_3| = {len(S3)}. Found {len(subgroups)} subgroups.")
for H in subgroups:
    names = "{" + ", ".join(labels[p] for p in H) + "}"
    assert len(S3) % len(H) == 0, "Lagrange violated!"
    print(f"  |H| = {len(H)} divides 6  ->  {names}")
print("Lagrange's theorem confirmed: every subgroup order divides |G|.")
