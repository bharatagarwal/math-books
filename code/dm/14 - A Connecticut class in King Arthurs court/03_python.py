# uv run --with networkx python
#
# FIGURE 48: "A bigraph with a perfect matching and one without."
#
# The chapter directs the reader to two bipartite graphs:
#   * G  -- HAS a perfect matching (the book draws it with heavy lines);
#   * H  -- has NO perfect matching, and the chapter says to "consider the
#           four black points and their neighbours" to see why.
#
# That instruction is exactly Hall's condition: four black nodes whose
# neighbours number fewer than four.  We reproduce both bigraphs, confirm G
# is perfectly matchable, confirm H is not, and pull out the "four black
# points" deficient set as the easily-checked certificate of non-existence.

import networkx as nx
from itertools import combinations


def is_perfect(G, top):
    M = nx.bipartite.hopcroft_karp_matching(G, top_nodes=top)
    return len(M) // 2 == len(top), M


def hall_violator(G, top):
    """Find a subset X of `top` with |N(X)| < |X| (Hall / Frobenius witness)."""
    for r in range(1, len(top) + 1):
        for X in combinations(top, r):
            nbrs = set()
            for x in X:
                nbrs.update(G.neighbors(x))
            if len(nbrs) < len(X):
                return set(X), nbrs
    return None, None


# ---- Graph G: a 4+4 bigraph that DOES have a perfect matching ----
G = nx.Graph()
topG = [f"a{i}" for i in range(4)]
botG = [f"b{i}" for i in range(4)]
G.add_nodes_from(topG, bipartite=0)
G.add_nodes_from(botG, bipartite=1)
# Each a_i can reach b_i (and a few extras) -> a perfect matching down the
# diagonal.
G.add_edges_from([
    ("a0", "b0"), ("a0", "b1"),
    ("a1", "b1"), ("a1", "b2"),
    ("a2", "b2"), ("a2", "b3"),
    ("a3", "b3"), ("a3", "b0"),
])
okG, MG = is_perfect(G, topG)
print("Graph G:")
print("  perfect matching exists:", okG)
assert okG
pairs = sorted((u, v) for u, v in MG.items() if u in topG)
print("  matching (heavy lines):", pairs)

# ---- Graph H: the "four black points" share too few neighbours ----
H = nx.Graph()
topH = [f"x{i}" for i in range(4)]   # the FOUR BLACK POINTS
botH = [f"y{i}" for i in range(4)]
H.add_nodes_from(topH, bipartite=0)
H.add_nodes_from(botH, bipartite=1)
# All four black points x0..x3 are only adjacent to y0, y1, y2 (three nodes).
H.add_edges_from([(x, y) for x in topH for y in ["y0", "y1", "y2"]])
okH, _ = is_perfect(H, topH)
print("\nGraph H:")
print("  perfect matching exists:", okH)
assert not okH

X, NX = hall_violator(H, topH)
print(f"  the four black points X = {sorted(X)}")
print(f"  their neighbours N(X) = {sorted(NX)}  "
      f"(|N(X)| = {len(NX)} < |X| = {len(X)})")
assert len(X) == 4 and len(NX) == 3
print("  Hall violated: 4 black points share only 3 neighbours -> no perfect")
print("  matching.  Exhibiting X is the EASY proof Frobenius' theorem "
      "promises.")
