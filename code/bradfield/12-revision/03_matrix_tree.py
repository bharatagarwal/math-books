# uv run --with numpy --with scipy --with networkx python \
#   code/bradfield/12-revision/03_matrix_tree.py
# CAPSTONE (graphs + linear algebra + determinants): Kirchhoff's Matrix-Tree
# theorem. The number of spanning trees of a graph equals any cofactor of its
# Laplacian -- AND the product of the Laplacian's nonzero eigenvalues over n.
import itertools
import numpy as np
import networkx as nx

G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (2, 3)])
n = G.number_of_nodes()

# Laplacian L = D - A (degree matrix minus adjacency).
L = nx.laplacian_matrix(G).toarray().astype(float)

# (1) Delete one row and column, take the determinant: that's the count.
cofactor = round(np.linalg.det(L[1:, 1:]))

# (2) Product of the n-1 nonzero eigenvalues, divided by n.
eigs = sorted(np.linalg.eigvalsh(L))      # smallest is ~0
by_eigs = round(float(np.prod(eigs[1:]) / n))

# Ground truth: brute-force count edge subsets of size n-1 that span as a tree.
edges = list(G.edges())
brute = 0
for sub in itertools.combinations(edges, n - 1):
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    H.add_edges_from(sub)
    if nx.is_tree(H):
        brute += 1

assert cofactor == by_eigs == brute

print("spanning trees -- cofactor:", cofactor, " eigenvalue product:", by_eigs,
      " brute force:", brute)
