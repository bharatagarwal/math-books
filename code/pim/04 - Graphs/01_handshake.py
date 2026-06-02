# uv run --with networkx --with scipy python \
#   "code/pim/04 - Graphs/01_handshake.py"
"""Lemma 6.8 (the handshake lemma): 2m = sum of degrees.

Every edge has two endpoints, so summing degrees double-counts
the edges.  We check it on a handful of graphs, including the
Petersen graph that recurs throughout the chapter.
"""
import networkx as nx


def check_handshake(G):
    m = G.number_of_edges()
    degree_sum = sum(d for _, d in G.degree())
    assert degree_sum == 2 * m, (degree_sum, 2 * m)
    return m, degree_sum


graphs = {
    "Petersen": nx.petersen_graph(),
    "K5": nx.complete_graph(5),
    "K3,3": nx.complete_bipartite_graph(3, 3),
    "cycle C6": nx.cycle_graph(6),
    "star S7": nx.star_graph(7),  # 1 hub + 7 leaves
}

for name, G in graphs.items():
    m, s = check_handshake(G)
    print(f"{name:>10}: m={m:2d}, sum(deg)={s:2d}, 2m={2 * m:2d}")

print("\nAll graphs satisfy 2m = sum(deg).")
