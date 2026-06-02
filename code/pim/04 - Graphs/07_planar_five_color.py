# uv run --with networkx --with scipy python \
#   "code/pim/04 - Graphs/07_planar_five_color.py"
"""Section 6.5: the recursive 5-coloring algorithm from the proof
of the Five Color Theorem (Theorem 6.7).

Kun's book uses igraph; we re-implement the same algorithm with
networkx so it runs out of the box.  The structure mirrors the
proof exactly:

  * base case: <= 5 vertices get distinct colors;
  * find a vertex v of degree <= 5 (Lemma 6.10 guarantees one);
  * if deg(v) <= 4, recurse on G - v and pick a free color;
  * if deg(v) = 5, find two non-adjacent neighbors w_i, w_j
    (they exist because K5 is not planar), merge them, recurse,
    then split the shared color back out and color v.

We test it on the icosahedron (Figure 6.10): a planar graph in
which *every* vertex has degree 5, so the hard branch fires.
"""
from itertools import combinations
import networkx as nx

COLORS = list(range(5))


def find_two_nonadjacent(G, nodes):
    for x, y in combinations(nodes, 2):
        if not G.has_edge(x, y):
            return x, y
    raise ValueError("all pairs adjacent -- would be K5, impossible")


def planar_five_color(G):
    G = G.copy()
    n = G.number_of_nodes()
    if n <= 5:                                    # base case
        return {v: c for v, c in zip(G.nodes(), COLORS[:n])}

    # Lemma 6.10: some vertex has degree <= 5.
    v = min(G.nodes(), key=lambda u: G.degree(u))
    assert G.degree(v) <= 5, "planar graph must have a vertex deg<=5"

    if G.degree(v) <= 4:                          # easy case
        H = G.copy()
        H.remove_node(v)
        coloring = planar_five_color(H)
        used = {coloring[w] for w in G.neighbors(v)}
        coloring[v] = next(c for c in COLORS if c not in used)
        return coloring

    # Hard case: deg(v) = 5.  Merge two non-adjacent neighbors.
    nbrs = list(G.neighbors(v))
    wi, wj = find_two_nonadjacent(G, nbrs)
    H = G.copy()
    H.remove_node(v)
    H = nx.contracted_nodes(H, wi, wj, self_loops=False)  # wj -> wi
    coloring = planar_five_color(H)

    full = {}
    for u in coloring:                # spread H's colors back to G
        full[u] = coloring[u]
    full[wj] = coloring[wi]           # the merged pair shares a color
    used = {full[w] for w in G.neighbors(v)}
    full[v] = next(c for c in COLORS if c not in used)
    return full


def is_proper(G, coloring):
    return all(coloring[u] != coloring[v] for u, v in G.edges())


for name, G in [("triangle", nx.complete_graph(3)),
                ("wheel W6", nx.wheel_graph(6)),
                ("cube Q3", nx.hypercube_graph(3)),
                ("icosahedron", nx.icosahedral_graph())]:
    assert nx.check_planarity(G)[0], f"{name} must be planar"
    coloring = planar_five_color(G)
    assert set(coloring) == set(G.nodes()), "every vertex colored"
    assert is_proper(G, coloring), f"{name} coloring not proper"
    assert max(coloring.values()) < 5, "used more than 5 colors"
    k = len(set(coloring.values()))
    print(f"{name:>12}: properly colored with {k} <= 5 colors")

print("\nEvery planar graph above is 5-colored, including the "
      "5-regular icosahedron (the deg-5 branch).")
