# uv run python "code/pim/09 - Groups/06_cayley_theorem.py"
"""Cayley's theorem: every group embeds in a symmetric group.

Section 16.4 ends with a gem: every group G has a homomorphism
f: G -> S(G) where a in G becomes the bijection x |-> a*x. Its kernel
is trivial, so G is isomorphic to im f, a subgroup of S(G). We make
this concrete for G = Z/5Z: each element becomes a permutation of the
5 elements, the map is an injective homomorphism, and the image is a
genuine subgroup of the symmetric group on 5 points.
"""

n = 5
G = list(range(n))


def left_mult_perm(a):
    """The permutation x |-> (a + x) mod n, as a tuple."""
    return tuple((a + x) % n for x in G)


def compose(p, q):
    return tuple(p[q[i]] for i in range(n))


f = {a: left_mult_perm(a) for a in G}

# Homomorphism: f(a + b) == f(a) o f(b).
for a in G:
    for b in G:
        assert f[(a + b) % n] == compose(f[a], f[b])
print("f(a+b) = f(a) o f(b): the map G -> S(G) is a homomorphism.")

# Injective (trivial kernel): only 0 maps to the identity permutation.
identity_perm = tuple(G)
kernel = [a for a in G if f[a] == identity_perm]
assert kernel == [0]
print("ker f = {0}: f is injective, so G ~= im f.")

# The image is a set of 5 distinct permutations -- a subgroup of S_5.
image = set(f.values())
assert len(image) == n
for p in image:
    for q in image:
        assert compose(p, q) in image
print(f"im f has {len(image)} permutations, closed under composition:")
for a in G:
    print(f"  {a} -> {f[a]}")
print("So Z/5Z is (isomorphic to) a subgroup of the symmetric group S_5.")
