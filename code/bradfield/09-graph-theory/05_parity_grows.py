# uv run --with scipy --with networkx python \
#   code/bradfield/09-graph-theory/05_parity_grows.py
# INTUITION (LL ch 9, Theorem 9.1, Figure 17): build a graph one edge at a
# time and WATCH the count of odd-degree nodes stay even at every step --
# the "one edge at a time" induction made visible, not just asserted.
import random
import networkx as nx


def num_odd(g):
    return sum(1 for _, d in g.degree() if d % 2 == 1)


# Add the edges of Figure 14's party (Alice..Eve) one at a time and print the
# running odd-degree count. Each new edge flips the parity of its two ends, so
# the count changes by -2, 0, or +2 -- never by an odd amount.
names = ["Alice", "Bob", "Carl", "Diane", "Eve"]
party = [("Alice", "Bob"), ("Alice", "Carl"), ("Alice", "Diane"),
         ("Alice", "Eve"), ("Bob", "Carl"), ("Carl", "Eve")]
G = nx.Graph()
G.add_nodes_from(names)
print("growing the party graph edge by edge (Figure 17 in action):")
print(f"  start (no edges): #odd = {num_odd(G)}")
for u, v in party:
    before = num_odd(G)
    G.add_edge(u, v)
    after = num_odd(G)
    delta = after - before
    assert delta in (-2, 0, 2)        # parity changes by an even amount
    assert after % 2 == 0             # ... so the count stays even
    print(f"  +{u[0]}{v[0]}: #odd {before} -> {after}  (change {delta:+d})")

# The final degrees reproduce the book: A4 B2 C3 D1 E2 -> three even, one odd?
# No: Carl(3) and Diane(1) are odd -> exactly TWO odd-degree nodes (even count).
final = dict(G.degree())
print("final degrees:", {n[0]: final[n] for n in names})
assert num_odd(G) == 2

# Now stress the SAME mechanism on many random growth orders and graphs: at no
# intermediate step is the odd-degree count ever odd.
rng = random.Random(42)
for _ in range(2000):
    k = rng.randint(2, 7)
    g = nx.Graph()
    g.add_nodes_from(range(k))
    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
    rng.shuffle(pairs)
    for i, j in pairs[: rng.randint(0, len(pairs))]:
        g.add_edge(i, j)
        assert num_odd(g) % 2 == 0    # invariant after every single edge
print("invariant '#odd-degree nodes is even' held after every edge,",
      "over 2000 random growth sequences")
