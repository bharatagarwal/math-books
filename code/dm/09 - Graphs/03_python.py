# uv run --with networkx python
#
# Section 9.2: paths, cycles, complete graphs, and connectivity.
# We build the three "special graphs" the book names and check their defining
# counts, then exhibit connectivity via concrete paths and connected components.

import networkx as nx
from itertools import combinations

n = 5

# Complete graph K_n: connect every pair. The book says it has C(n,2) edges.
K = nx.complete_graph(n)
expected_edges = n * (n - 1) // 2  # = C(n,2)
print(f"K_{n}: |E| = {K.number_of_edges()}, C({n},2) = {expected_edges}, "
      f"connected = {nx.is_connected(K)}")
assert K.number_of_edges() == expected_edges
assert nx.is_connected(K)

# Path on n nodes: connect consecutive nodes in a row -> n-1 edges, two
# endpoints of degree 1, the rest of degree 2.
P = nx.path_graph(n)
endpoints = [v for v, d in P.degree() if d == 1]
print(f"path P_{n}: |E| = {P.number_of_edges()} (expect {n-1}), "
      f"endpoints (deg 1) = {endpoints}")
assert P.number_of_edges() == n - 1
assert len(endpoints) == 2

# Cycle on n nodes: also connect the last node back to the first -> n edges,
# every degree is 2.
C = nx.cycle_graph(n)
cycle_degrees = sorted(d for _, d in C.degree())
print(f"cycle C_{n}: |E| = {C.number_of_edges()} (expect {n}), "
      f"degrees = {cycle_degrees}")
assert C.number_of_edges() == n
assert all(d == 2 for _, d in C.degree())

# Connectivity: a graph is connected iff every two nodes are joined by a path.
# Verify the definition directly on the path graph by finding an a--b path
# for *every* pair of nodes.
for a, b in combinations(P.nodes(), 2):
    assert nx.has_path(P, a, b)
print(f"P_{n} is connected = {nx.is_connected(P)} (every pair has a path)")
assert nx.is_connected(P)

# A disconnected graph and its connected components (Section 9.2):
# two triangles plus an isolated node -> three components.
D = nx.Graph()
D.add_edges_from([(0, 1), (1, 2), (2, 0),       # triangle A
                  (3, 4), (4, 5), (5, 3)])       # triangle B
D.add_node(6)                                    # isolated node
comps = [sorted(c) for c in nx.connected_components(D)]
n_comps = nx.number_connected_components(D)
print(f"disconnected graph -> {n_comps} components: {sorted(comps)}")
assert nx.number_connected_components(D) == 3
# Exercise 9.16: no edge connects nodes in different components.
comp_id = {v: i for i, c in enumerate(nx.connected_components(D)) for v in c}
assert all(comp_id[u] == comp_id[v] for u, v in D.edges())
print("OK: no edge crosses between components (exercise 9.16).")
