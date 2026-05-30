# uv run --with networkx python
#
# Trees as graphs (Section 10) + Cayley's Theorem (Theorem 10.5).
#
# Two things this verifies against the book:
#   1. The defining properties of a tree (connected, no cycle) and the
#      consequence n-1 edges (Theorem 10.4), checked on the labelled tree
#      of Figure 24.
#   2. Cayley's count n^(n-2) of LABELLED trees, by brute-force enumerating
#      every tree on n nodes and confirming the totals are exactly the
#      book's numbers 1, 1, 3, 16, 125 for n = 2, 3, 4, 5 (and 1296 for n=6).
import itertools
import networkx as nx


def figure_24_tree():
    # Figure 24, given by its "father code" table (node : father):
    #   1->6  2->0  3->0  4->2  5->6  6->2  7->9  8->9  9->2
    edges = [(1, 6), (2, 0), (3, 0), (4, 2), (5, 6),
             (6, 2), (7, 9), (8, 9), (9, 2)]
    G = nx.Graph()
    G.add_nodes_from(range(10))
    G.add_edges_from(edges)
    return G


def count_labelled_trees(n):
    """Brute force: keep every (n-1)-edge subgraph that nx calls a tree."""
    if n == 1:
        return 1
    nodes = list(range(n))
    all_edges = list(itertools.combinations(nodes, 2))
    total = 0
    for es in itertools.combinations(all_edges, n - 1):
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(es)
        if nx.is_tree(G):
            total += 1
    return total


def main():
    G = figure_24_tree()
    n = G.number_of_nodes()
    print("Figure 24 tree:")
    print(f"  nodes = {n}, edges = {G.number_of_edges()}")
    print(f"  is_tree (connected & acyclic) = {nx.is_tree(G)}")
    print(f"  Theorem 10.4 (edges == n-1)   = {G.number_of_edges() == n - 1}")
    # Theorem 10.2: at least two nodes of degree 1 (leaves).
    leaves = [v for v in G.nodes() if G.degree(v) == 1]
    print(f"  leaves (deg-1 nodes) = {sorted(leaves)}"
          f"  (>= 2: {len(leaves) >= 2})")

    print("\nCayley's Theorem: # labelled trees on n nodes == n^(n-2)")
    print(f"  {'n':>2} | {'enumerated':>10} | {'n^(n-2)':>8} | match")
    for k in range(1, 7):
        c = count_labelled_trees(k)
        cay = 1 if k == 1 else k ** (k - 2)
        print(f"  {k:>2} | {c:>10} | {cay:>8} | {c == cay}")


if __name__ == "__main__":
    main()
