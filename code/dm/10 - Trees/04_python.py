# uv run --with networkx --with numpy python
#
# Cayley's Theorem, a second way: the labelled trees on n nodes are exactly
# the SPANNING TREES of the complete graph K_n. So Cayley says K_n has
# n^(n-2) spanning trees -- which the Matrix-Tree Theorem (Kirchhoff) lets
# us compute as a single determinant, with no enumeration at all.
#
# Matrix-Tree: #spanning trees = any cofactor of the Laplacian L = D - A.
# For K_n the Laplacian gives the cofactor n^(n-2), matching the book's
# 1, 3, 16, 125, 1296 for n = 3, 4, 5, 6. We also enumerate spanning trees
# directly for tiny n as a cross-check, and find a minimum spanning tree of
# a small weighted graph (the "cheapest road network" reading of Section 10).
import networkx as nx
import numpy as np


def spanning_trees_via_matrix_tree(n):
    """Kirchhoff: delete one row+col of the Laplacian of K_n, take det.
    Build L = D - A with numpy (no scipy): for K_n, A is all-ones off-diagonal
    and D = (n-1)*I."""
    A = np.ones((n, n)) - np.eye(n)
    D = np.diag(A.sum(axis=1))
    L = D - A
    minor = L[1:, 1:]  # delete row/col 0
    return round(np.linalg.det(minor))


def main():
    print("K_n spanning trees  ==  labelled trees on n nodes  ==  n^(n-2)")
    print(f"  {'n':>2} | {'matrix-tree det':>15} | {'n^(n-2)':>8} | match")
    for n in range(3, 7):
        mt = spanning_trees_via_matrix_tree(n)
        cay = n ** (n - 2)
        print(f"  {n:>2} | {mt:>15} | {cay:>8} | {mt == cay}")

    # Cross-check by brute enumeration of spanning trees for tiny n.
    print("\nDirect enumeration of spanning trees of K_n (cross-check):")
    for n in range(3, 6):
        Kn = nx.complete_graph(n)
        cnt = sum(1 for _ in nx.SpanningTreeIterator(Kn))
        cay = n ** (n - 2)
        print(f"  n={n}: {cnt} spanning trees"
              f" (n^(n-2) = {cay}) -> {cnt == cay}")

    # Section 10 reading: a tree as the cheapest road network connecting towns.
    print("\nMinimum spanning tree of a small weighted 'road' graph:")
    W = nx.Graph()
    W.add_weighted_edges_from([
        (0, 1, 4), (0, 2, 1), (1, 2, 2), (1, 3, 5),
        (2, 3, 8), (3, 4, 3), (2, 4, 7),
    ])
    mst = nx.minimum_spanning_tree(W)
    total = sum(d["weight"] for _, _, d in mst.edges(data=True))
    n_minus_1 = W.number_of_nodes() - 1
    print(f"  MST is a tree: {nx.is_tree(mst)}"
          f"  edges = {mst.number_of_edges()} (= n-1 = {n_minus_1})")
    print(f"  MST edges = {sorted(tuple(sorted(e)) for e in mst.edges())}")
    print(f"  total weight = {total}")


if __name__ == "__main__":
    main()
