# uv run --with numpy python \
#   "code/pim/07 - Eigenvectors and Eigenvalues/01_graph_eigenvalues.py"
# Theorem 12.4: a connected graph is bipartite iff lambda_1 = -lambda_n,
# where lambda_1 is the largest and lambda_n the smallest eigenvalue of
# the adjacency matrix. We build Kun's Figure 12.1 graph and check it.
import numpy as np


def adjacency(n, edges):
    """A(G): symmetric 0/1 matrix, A[i,j]=1 iff (i,j) is an edge."""
    A = np.zeros((n, n))
    for i, j in edges:
        A[i, j] = A[j, i] = 1
    return A


# Figure 12.1: vertices 1..5 (0-indexed here), edges 1-2, 1-4, 1-5, 3-4.
G_edges = [(0, 1), (0, 3), (0, 4), (2, 3)]
A = adjacency(5, G_edges)
print("A(G) =")
print(A.astype(int))

# Adjacency matrices are symmetric, so eigenvalues are real (Thm 12.6).
eigs = np.sort(np.linalg.eigvalsh(A))  # ascending
lam_n, lam_1 = eigs[0], eigs[-1]
print("eigenvalues:", np.round(eigs, 4))
print(f"lambda_1 = {lam_1:.4f}, lambda_n = {lam_n:.4f}")

# Kun's Fig 12.1 graph is bipartite: parts {1,3} and {2,4,5}.
is_bipartite = np.isclose(lam_1, -lam_n)
print("lambda_1 == -lambda_n ?", is_bipartite)
assert is_bipartite, "Figure 12.1 graph should be bipartite"

# A triangle (the complete graph K_3) is the canonical non-bipartite
# graph -- it has an odd cycle. Its spectrum is NOT symmetric.
K3 = adjacency(3, [(0, 1), (1, 2), (0, 2)])
e3 = np.sort(np.linalg.eigvalsh(K3))
print("\nK_3 eigenvalues:", np.round(e3, 4))
assert not np.isclose(e3[-1], -e3[0]), "K_3 is not bipartite"
print("K_3 is not bipartite (lambda_1 != -lambda_n), as expected.")

print("\nTheorem 12.4 verified on both graphs.")
