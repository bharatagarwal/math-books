# uv run --with networkx --with scipy python \
#   "code/pim/04 - Graphs/06_planarity_bound.py"
"""Lemma 6.9 / Lemma 6.10 consequence: every simple planar graph
satisfies |E| <= 3|V| - 6.

This is the bound that proves K5 is not planar (it has 10 edges
but 3*5 - 6 = 9) and underlies "every planar graph has a vertex of
degree at most 5."  We confirm the bound holds for planar graphs
and is violated by K5 and K3,3 (which is why they fail to embed).
"""
import networkx as nx


def edge_bound(G):
    V = G.number_of_nodes()
    E = G.number_of_edges()
    return E, 3 * V - 6


def min_degree(G):
    return min((d for _, d in G.degree()), default=0)


print("Planar graphs (bound |E| <= 3|V| - 6 must hold):")
for name, G in [("K4", nx.complete_graph(4)),
                ("cube Q3", nx.hypercube_graph(3)),
                ("icosahedron", nx.icosahedral_graph())]:
    E, bound = edge_bound(G)
    planar, _ = nx.check_planarity(G)
    assert planar and E <= bound, (name, E, bound)
    # Lemma 6.10: a planar graph has a vertex of degree <= 5.
    assert min_degree(G) <= 5
    print(f"  {name:>12}: |E|={E:2d} <= 3|V|-6={bound:2d}  "
          f"(min degree {min_degree(G)} <= 5)")

print("\nNon-planar graphs (bound is violated, so they can't embed):")
for name, G in [("K5", nx.complete_graph(5)),
                ("K3,3", nx.complete_bipartite_graph(3, 3))]:
    E, bound = edge_bound(G)
    planar, _ = nx.check_planarity(G)
    note = "" if name != "K3,3" else "  (needs the triangle-free bound)"
    print(f"  {name:>12}: |E|={E:2d}, 3|V|-6={bound:2d}, "
          f"planar? {planar}{note}")

# K5 fails the bound directly; that is Kun's "bonus fact".
assert nx.complete_graph(5).number_of_edges() > 3 * 5 - 6
assert not nx.check_planarity(nx.complete_graph(5))[0]
print("\nK5: 10 > 9 = 3*5-6, so K5 is not planar.")
