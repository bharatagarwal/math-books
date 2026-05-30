# uv run --with networkx python
#
# The party graph of Figure 14, encoded exactly as the book describes it:
#   Alice knows everybody else; Bob and Carl know each other; Carl
#   also knows Eve.
# We read off the degrees (the book gets Alice 4, Bob 2, Carl 3,
# Diane 1, Eve 2), count how many are even, and verify Theorem 9.2:
# sum(deg) = 2|E|.

import networkx as nx

G = nx.Graph()
G.add_nodes_from(["Alice", "Bob", "Carl", "Diane", "Eve"])
# Alice knows everybody else
G.add_edges_from([("Alice", "Bob"), ("Alice", "Carl"),
                  ("Alice", "Diane"), ("Alice", "Eve")])
# Bob and Carl know each other
G.add_edge("Bob", "Carl")
# Carl also knows Eve
G.add_edge("Carl", "Eve")

deg = dict(G.degree())
print("degrees:", {name: deg[name] for name in
                   ["Alice", "Bob", "Carl", "Diane", "Eve"]})

# Reproduce the book's numbers exactly.
assert deg["Alice"] == 4
assert deg["Bob"] == 2
assert deg["Carl"] == 3
assert deg["Diane"] == 1
assert deg["Eve"] == 2

even_nodes = [v for v, d in deg.items() if d % 2 == 0]
odd_nodes = [v for v, d in deg.items() if d % 2 == 1]
print("even-degree nodes:", sorted(even_nodes), "-> count", len(even_nodes))
print("odd-degree  nodes:", sorted(odd_nodes), "-> count", len(odd_nodes))

# Book: three people with an even number of acquaintances (Alice, Bob, Eve).
assert len(even_nodes) == 3

# Theorem 9.1: number of odd-degree nodes is even.
assert len(odd_nodes) % 2 == 0

# Theorem 9.2: the sum of degrees equals twice the number of edges.
deg_sum = sum(deg.values())
num_edges = G.number_of_edges()
print(f"sum(deg) = {deg_sum}, 2*|E| = {2 * num_edges}, |E| = {num_edges}")
assert deg_sum == 2 * num_edges

print("OK: reproduced Figure 14; Theorem 9.1 and Theorem 9.2 hold.")
