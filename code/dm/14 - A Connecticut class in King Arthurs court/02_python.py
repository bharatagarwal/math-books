# uv run --with z3-solver python
#
# The SEATING problem (the chapter's second tale).
#
# Seat the knights around the ROUND TABLE so that each knight sits between two
# FRIENDS.  A round seating where every neighbour is a friend is exactly a
# HAMILTON CYCLE in the friendship graph: a cyclic order visiting every knight
# once, consecutive knights joined by a friendship edge.
#
# The chapter's punchline: if SOME knight has only ONE friend (a degree-1 node),
# the impossibility has a "simple reason" -- that knight needs two friendly
# neighbours at the table but only has one friend, so no seating works, and
# even King Arthur can see it.  But in general no such simple certificate
# exists.
#
# We model the seating as an SMT constraint problem and let z3 (a) FIND a valid
# round-table seating when one exists (the easy-to-check NP certificate Merlin
# hopes for), and (b) prove UNSAT for a court containing a lonely knight.

from z3 import Solver, Int, Distinct, And, Or, sat


def seat_round_table(friends, n, names):
    """Seat knights 0..n-1 round a table so neighbours are friends.

    friends: set of frozenset({i, j}) friendship pairs.
    Returns a seating order (list of knight ids) or None if impossible.
    """
    # pos[i] = the seat (0..n-1) assigned to knight i; seats form a cycle.
    pos = [Int(f"pos_{i}") for i in range(n)]
    s = Solver()
    for p in pos:
        s.add(And(p >= 0, p < n))
    s.add(Distinct(pos))  # every knight a distinct seat == a permutation

    def friendly(i, j):
        return frozenset({i, j}) in friends

    # For each ORDERED pair, if they sit in consecutive seats (cyclically) they
    # must be friends.  Seats a and b are cyclically adjacent iff
    # (a - b) mod n == 1, i.e. b == a+1 or a == b+1 (with wraparound).
    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            adj = Or(pos[i] - pos[j] == 1, pos[j] - pos[i] == 1,
                     pos[i] - pos[j] == n - 1, pos[j] - pos[i] == n - 1)
            if not friendly(i, j):
                # non-friends must NOT be cyclic neighbours
                s.add(adj == False)

    if s.check() != sat:
        return None
    m = s.model()
    seat_of = {i: m[pos[i]].as_long() for i in range(n)}
    order = sorted(range(n), key=lambda i: seat_of[i])  # knights by seat
    return [names[i] for i in order]


# ---- Case A: a friendly court that CAN be seated (Hamilton cycle exists) ----
names_A = ["Arthur", "Lancelot", "Gawain", "Percival", "Galahad", "Bors"]
nA = len(names_A)
# Friendship graph = the 6-cycle plus a couple of chords; a Hamilton cycle
# exists.
edges_A = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3), (1, 4)]
friends_A = {frozenset(e) for e in edges_A}

order = seat_round_table(friends_A, nA, names_A)
print("Case A (a friendly court):")
assert order is not None, "should be seatable"
ring = order + [order[0]]
print("  round-table order:", " -> ".join(ring))
# Verify the found seating ourselves: every cyclic neighbour pair is a friend.
idx = {name: i for i, name in enumerate(names_A)}
for a, b in zip(ring, ring[1:]):
    assert frozenset({idx[a], idx[b]}) in friends_A, f"{a},{b} are not friends!"
print("  verified: every pair of neighbours is friends -> valid seating "
      "(NP certificate).")

# ---- Case B: a court with a LONELY knight (the chapter's "simple reason") ----
names_B = ["Arthur", "Lancelot", "Gawain", "Percival", "Kay"]
nB = len(names_B)
# "Kay" (id 4) is friends with only ONE other knight -> degree 1.
edges_B = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (3, 4)]  # Kay-Percival only
friends_B = {frozenset(e) for e in edges_B}
deg_kay = sum(1 for e in friends_B if 4 in e)
print("\nCase B (Sir Kay has only", deg_kay, "friend):")
order_B = seat_round_table(friends_B, nB, names_B)
assert order_B is None, "a degree-1 knight makes any round seating impossible"
print("  z3 proves UNSAT -> NO valid round-table seating exists.")
print("  The 'simple reason': a knight with one friend needs two friendly")
print("  table-neighbours but has only one -> even King Arthur sees it.")
