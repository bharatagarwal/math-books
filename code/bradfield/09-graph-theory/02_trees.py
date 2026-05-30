# uv run --with scipy --with networkx python \
#   code/bradfield/09-graph-theory/02_trees.py
# Trees: the minimal connected graphs. Several definitions, one object.
import itertools
import networkx as nx

T = nx.Graph()
T.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4)])
n = T.number_of_nodes()

# Equivalent characterizations of a tree (any two imply the rest):
#   connected, acyclic, and exactly n-1 edges.
assert nx.is_tree(T)
assert nx.is_connected(T)
assert T.number_of_edges() == n - 1

# A defining property: between any two vertices there is exactly one
# simple path (LL exercise 10.3).
for a, b in itertools.combinations(T.nodes(), 2):
    assert len(list(nx.all_simple_paths(T, a, b))) == 1

# Trees are critically balanced: add any edge -> a cycle appears (no longer a
# tree); remove any edge -> it disconnects.
with_cycle = T.copy()
with_cycle.add_edge(3, 4)
assert not nx.is_tree(with_cycle)

disconnected = T.copy()
disconnected.remove_edge(0, 1)
assert not nx.is_connected(disconnected)

print(f"tree on {n} nodes has {T.number_of_edges()} = n-1 edges, "
      "unique paths, and is edge-critical")
