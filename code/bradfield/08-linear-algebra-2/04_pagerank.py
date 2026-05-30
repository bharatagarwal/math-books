# uv run --with scipy --with numpy --with networkx python \
#   code/bradfield/08-linear-algebra-2/04_pagerank.py
#
# PageRank = the dominant eigenvector of the "Google matrix".
# Model a surfer who 85% of the time follows a random outgoing
# link and 15% teleports to a random page. The ranking r is the
# stationary distribution G r = r, i.e. the eigenvector for
# eigenvalue 1. We build G by hand, find r by power iteration
# (the engine from 07), and cross-check against networkx.
import numpy as np
import networkx as nx

# A tiny link graph: edge i->j means page i links to page j.
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (3, 2)]
n = 4
M = np.zeros((n, n))
for i, j in edges:
    M[j, i] = 1.0  # column i = where page i sends its weight
for col in range(n):
    s = M[:, col].sum()
    if s == 0:
        M[:, col] = 1.0 / n   # dangling page -> spread evenly
    else:
        M[:, col] /= s

d = 0.85
G = d * M + (1 - d) / n * np.ones((n, n))
assert np.allclose(G.sum(axis=0), 1.0)  # columns are stochastic

# Power iteration: G r = r is the eigenvalue-1 eigenvector.
r = np.ones(n) / n
for _ in range(200):
    r = G @ r
r /= r.sum()
assert np.allclose(G @ r, r, atol=1e-9)  # stationary

# Cross-check against networkx's PageRank.
Gx = nx.DiGraph(edges)
ref = nx.pagerank(Gx, alpha=d)
ref = np.array([ref[i] for i in range(n)])
assert np.allclose(r, ref, atol=1e-4)

order = np.argsort(-r)
print("page  rank (power iter)  networkx")
for i in range(n):
    print(f"  {i}      {r[i]:.4f}          {ref[i]:.4f}")
print(f"ranking, most to least important: {list(order)}")
print("importance on a graph is an eigenvector problem")
