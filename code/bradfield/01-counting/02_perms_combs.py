# uv run --with sympy python code/bradfield/01-counting/02_perms_combs.py
# The party's SMALL counts need no formula -- build the objects and count them.
# We enumerate, then cross-check against the closed form, so the two agree.
from itertools import permutations, combinations
from math import factorial, perm, comb

# Seatings of 6 guests with Alice's chair fixed (LL 2.1): 6! orderings.
guests = ["Bob", "Carl", "Diane", "Eve", "Frank", "George"]
seatings = list(permutations(guests))
assert len(seatings) == factorial(6) == 720

# Handshakes among 7 people = unordered pairs = C(7,2). Eve's "42/2".
people = guests + ["Alice"]
handshakes = list(combinations(people, 2))
assert len(handshakes) == comb(7, 2) == 7 * 6 // 2 == 21

# Chess matchings of 6 players into 3 unordered pairs, boards indistinguishable
# (Bob's sense). Build them by recursively pairing the lowest-indexed player.
def perfect_matchings(items):
    if not items:
        return [[]]
    first, rest = items[0], items[1:]
    out = []
    for i, partner in enumerate(rest):
        pair = (first, partner)
        for m in perfect_matchings(rest[:i] + rest[i + 1:]):
            out.append([pair] + m)
    return out

matchings = perfect_matchings(list(range(6)))
assert len(matchings) == 15                 # = 720 / 48 = 5*3 (LL's two arguments)
assert len(matchings) == factorial(6) // (factorial(3) * 2 ** 3)

# The general link behind all of it: ordered k-selections = C(n,k) * k!.
for k in range(0, 6):
    assert perm(5, k) == comb(5, k) * factorial(k)

print("seatings of 6 guests (Alice fixed) =", len(seatings))
print("handshakes among 7 people          =", len(handshakes))
print("chess matchings of 6 (Bob's sense) =", len(matchings))
print("identity P(n,k) = C(n,k)*k! holds for k = 0..5")
