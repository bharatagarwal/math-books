# uv run python "code/pim/09 - Groups/02_dihedral_square.py"
"""The symmetry group of the square, D_8, built from corner labels.

Kun shows a symmetry is *completely determined by how it acts on the
corners* A, B, C, D. So we represent each symmetry as a permutation
of the 4 corners and compose by following the permutations. Then we
verify Kun's three defining relations and reproduce, exactly, his
page-307 reduction of the word sigma rho^9 sigma rho^-3 sigma = sigma.
"""

# Corners A,B,C,D at indices 0,1,2,3, counterclockwise around the square.
# rho: counterclockwise quarter-turn sends corner at slot i to slot i+1.
# sigma: flip across the A-C diagonal swaps B and D, fixes A and C.
rho = (1, 2, 3, 0)        # new[i] = old position feeding slot i
sigma = (0, 3, 2, 1)


def compose(f, g):
    """Apply g first, then f (right-to-left, like function calls)."""
    return tuple(f[g[i]] for i in range(4))


identity = (0, 1, 2, 3)


def power(p, k):
    """p composed with itself k times; negative k uses the inverse."""
    if k < 0:
        p = inverse(p)
        k = -k
    out = identity
    for _ in range(k):
        out = compose(out, p)
    return out


def inverse(p):
    inv = [0] * 4
    for i, pi in enumerate(p):
        inv[pi] = i
    return tuple(inv)


# Kun's three relations.
assert power(rho, 4) == identity, "rho^4 != 1"
assert power(sigma, 2) == identity, "sigma^2 != 1"
assert compose(compose(rho, sigma), rho) == sigma, "rho sigma rho != sigma"
print("Relations hold: rho^4 = 1, sigma^2 = 1, rho sigma rho = sigma.")

# Generate the whole group from rho and sigma, confirm |D_8| = 8.
group = set()
frontier = [identity]
gens = [rho, sigma]
while frontier:
    x = frontier.pop()
    if x in group:
        continue
    group.add(x)
    for g in gens:
        frontier.append(compose(g, x))
print(f"<rho, sigma> generates {len(group)} symmetries (expected 8).")
assert len(group) == 8

# Reproduce the page-307 word reduction: sigma rho^9 sigma rho^-3 sigma.
word = sigma
for piece in [power(rho, 9), sigma, power(rho, -3), sigma]:
    word = compose(word, piece)
assert word == sigma, "word did not reduce to sigma"
print("sigma rho^9 sigma rho^-3 sigma  reduces to  sigma. Confirmed.")
