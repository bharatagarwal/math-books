# uv run python
# Brute-force enumeration vs. the closed forms from the party.
# Reproduces the book's numbers by *listing every arrangement* and counting:
#   - seat 6 guests with Alice fixed -> 6! = 720 seatings
#   - handshakes among 7 people      -> C(7,2) = 21
#   - chess matchings (Bob's sense)  -> 15 unordered perfect matchings of 6
# No closed-form formula is used here; we count the actual objects.

from itertools import permutations, combinations
from math import factorial

GUESTS = ["Bob", "Carl", "Diane", "Eve", "Frank", "George"]  # 6 guests
PEOPLE = ["Alice"] + GUESTS                                  # 7 people


def count_seatings():
    """Alice's chair is fixed; the 6 guests fill the other 6 chairs.
    A seating is an ordering of the 6 guests -> permutations enumerate them."""
    seatings = set(permutations(GUESTS))
    return len(seatings)


def count_handshakes():
    """Every handshake is an unordered pair of distinct people.
    Enumerating 2-subsets of the 7 people counts them once each."""
    pairs = list(combinations(PEOPLE, 2))
    return len(pairs)


def perfect_matchings(people):
    """Enumerate every way to split `people` into unordered pairs across
    indistinguishable boards (Bob's sense: order within a pair and order of
    boards do not matter). Recursively pair the lexicographically-first
    person with each remaining person."""
    if not people:
        yield ()
        return
    first, rest = people[0], people[1:]
    for i, partner in enumerate(rest):
        pair = (first, partner)
        remaining = rest[:i] + rest[i + 1:]
        for tail in perfect_matchings(remaining):
            yield (pair,) + tail


def count_matchings():
    return sum(1 for _ in perfect_matchings(PEOPLE[1:]))  # the 6 players


if __name__ == "__main__":
    s = count_seatings()
    h = count_handshakes()
    m = count_matchings()

    print(f"seatings of 6 guests (Alice fixed) = {s}  | 6! = {factorial(6)}")
    assert s == factorial(6) == 720

    print(f"handshakes among 7 people         = {h}  | C(7,2) = {7 * 6 // 2}")
    assert h == 21

    print(
        f"chess matchings of 6 (Bob's sense) = {m}"
        f"  | 5*3 = {5 * 3}, 720/48 = {720 // 48}"
    )
    assert m == 15

    print("all enumerations match the book's closed forms")
