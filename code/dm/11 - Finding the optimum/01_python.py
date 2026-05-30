# uv run --with networkx python
#
# Section 11.1, "Finding the best tree".
#
# The chapter describes THREE ways the lucky government can build the cheapest
# spanning tree and claims they all give the same minimum cost:
#   * the "optimistic"/greedy method = Kruskal (add the cheapest edge that does
#     not close a cycle),
#   * the capital-rooted growth of exercise 11.3 (always add the cheapest edge
#     leaving the already-built set S) = Prim,
#   * and the proof shows the result equals the true minimum over ALL trees.
#
# We reproduce all three on one weighted graph and confirm:
#   Kruskal cost == Prim cost == brute-force minimum over every spanning tree.
import itertools
import networkx as nx

# A small road network: 6 towns, costs are the given construction prices.
# (Costs are arbitrary positive numbers, exactly the setting of section 11.1.)
EDGES = [
    ("a", "b", 4), ("a", "c", 3), ("b", "c", 1), ("b", "d", 2),
    ("c", "d", 4), ("c", "e", 5), ("d", "e", 7), ("d", "f", 5),
    ("e", "f", 6), ("b", "e", 8),
]


def build():
    G = nx.Graph()
    for u, v, w in EDGES:
        G.add_edge(u, v, weight=w)
    return G


def brute_force_min_tree(G):
    """Cayley-style brute force: minimise over EVERY spanning tree."""
    nodes = list(G.nodes())
    edges = [(u, v) for u, v in G.edges()]
    best = None
    for combo in itertools.combinations(edges, len(nodes) - 1):
        H = nx.Graph()
        H.add_nodes_from(nodes)
        H.add_edges_from(combo)
        if nx.is_tree(H):
            cost = sum(G[u][v]["weight"] for u, v in combo)
            if best is None or cost < best:
                best = cost
    return best


def main():
    G = build()

    kruskal = nx.minimum_spanning_tree(G, algorithm="kruskal")
    # Prim = the capital-rooted growth of exercise 11.3.
    prim = nx.minimum_spanning_tree(G, algorithm="prim")

    k_cost = kruskal.size(weight="weight")
    p_cost = prim.size(weight="weight")
    bf_cost = brute_force_min_tree(G)

    print(f"Kruskal (optimistic/greedy) cost : {k_cost:g}")
    print(f"Prim    (capital-rooted, ex 11.3): {p_cost:g}")
    print(f"Brute force min over all trees   : {bf_cost:g}")

    assert k_cost == p_cost == bf_cost, "the three methods disagree!"
    # Kruskal and Prim may pick DIFFERENT edge sets but the COST is identical.
    print(f"All three agree on the minimum cost = {k_cost:g}")
    print(f"Kruskal edges: {sorted(tuple(sorted(e)) for e in kruskal.edges())}")
    print(f"Prim    edges: {sorted(tuple(sorted(e)) for e in prim.edges())}")


if __name__ == "__main__":
    main()
