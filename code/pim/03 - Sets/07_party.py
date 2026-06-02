# uv run python "code/pim/03 - Sets/07_party.py"
# The party puzzle, observed empirically: in ANY party of n > 1
# people with symmetric, irreflexive friendship, two people must
# have the same number of friends. We generate random friendship
# graphs and confirm the proof's conclusion holds every time.
import random


def random_party(n, rng):
    """Symmetric, irreflexive friendship as a set of edges."""
    friends = {i: set() for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < 0.5:
                friends[i].add(j)
                friends[j].add(i)
    return friends


def has_duplicate_friend_count(friends):
    counts = [len(friends[p]) for p in friends]
    return len(set(counts)) < len(counts)


rng = random.Random(0)
trials = 0
for n in range(2, 30):
    for _ in range(500):
        friends = random_party(n, rng)
        # The contradiction proof says a duplicate ALWAYS exists.
        assert has_duplicate_friend_count(friends)
        # Cross-check the proof's core fact: degrees 0 and n-1
        # never coexist (the loner vs. the universal friend).
        counts = {len(friends[p]) for p in friends}
        assert not (0 in counts and (n - 1) in counts)
        trials += 1

print(f"checked {trials} random parties; every one had a")
print("pair sharing a friend-count, as the proof guarantees")
