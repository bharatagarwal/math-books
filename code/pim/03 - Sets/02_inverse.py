# uv run python "code/pim/03 - Sets/02_inverse.py"
# A function f: A -> B is invertible exactly when it is a bijection.
# Here we build f as a SET of pairs (Definition 4.6), classify it,
# and -- when it is a bijection -- construct g and verify the two
# inverse laws from Definition 4.11: g(f(a)) = a and f(g(b)) = b.


def is_function(F, A):
    """Every a in A appears as the first coord of exactly one pair."""
    firsts = [a for (a, b) in F]
    return set(firsts) == set(A) and len(firsts) == len(set(firsts))


def is_injective(F):
    outs = [b for (a, b) in F]
    return len(outs) == len(set(outs))


def is_surjective(F, B):
    return set(b for (a, b) in F) == set(B)


def inverse(F):
    """Swap each pair; valid only when F is a bijection."""
    return {b: a for (a, b) in F}


A = [0, 1, 2, 3]
B = ["a", "b", "c", "d"]

# A genuine bijection on these sets.
f = [(0, "c"), (1, "a"), (2, "d"), (3, "b")]
assert is_function(f, A)
assert is_injective(f) and is_surjective(f, B)

fdict = dict(f)
g = inverse(f)
for a in A:
    assert g[fdict[a]] == a          # g(f(a)) = a
for b in B:
    assert fdict[g[b]] == b          # f(g(b)) = b
print("bijection f is invertible; both inverse laws check out")

# Squaring on {-2,-1,0,1,2} -> Z is NOT injective: 4 = (-2)^2 = 2^2.
sq = [(x, x * x) for x in [-2, -1, 0, 1, 2]]
assert not is_injective(sq)
# The preimage of 4 has size 2, matching the chapter's F^{-1}(4)={-2,2}.
preimage_4 = sorted(x for (x, y) in sq if y == 4)
assert preimage_4 == [-2, 2]
print("squaring is not injective; preimage of 4 is", preimage_4)
print("a non-injection has no inverse, as the chapter claims")
