# uv run --with networkx --with scipy python \
#   "code/pim/04 - Graphs/08_approx_coloring.py"
"""Section 6.6 / Theorem 6.11: color a 3-colorable graph with at
most 4*ceil(sqrt(n)) colors.

The algorithm (Wigderson's): while some uncolored vertex v has
degree >= sqrt(n), spend 3 fresh colors -- one for v, and two for
its neighborhood N(v), which must be 2-colorable because G is
3-colorable and v "uses up" one of the three colors.  Remove those
vertices.  When no high-degree vertex remains, finish greedily; the
max degree is then < sqrt(n), so greedy needs <= ceil(sqrt(n))
colors.  Total: <= 4*ceil(sqrt(n)).
"""
import math
import networkx as nx


def two_color(G):
    """Return a 2-coloring (offsets 0/1) of a bipartite graph G."""
    color = {}
    for comp in nx.connected_components(G):
        root = next(iter(comp))
        color[root] = 0
        stack = [root]
        while stack:
            u = stack.pop()
            for w in G.neighbors(u):
                if w not in color:
                    color[w] = 1 - color[u]
                    stack.append(w)
                elif color[w] == color[u]:
                    raise ValueError("not bipartite")
    return color


def approx_color_3colorable(G):
    n = G.number_of_nodes()
    threshold = math.sqrt(n)
    color = {}
    next_color = 0
    H = G.copy()

    while True:
        high = [v for v in H.nodes() if H.degree(v) >= threshold]
        if not high:
            break
        v = high[0]
        nbrs = list(H.neighbors(v))
        # N(v) is 2-colorable (G is 3-colorable, v takes one color).
        sub = H.subgraph(nbrs)
        sub_color = two_color(sub)
        color[v] = next_color
        for w, off in sub_color.items():
            color[w] = next_color + 1 + off
        next_color += 3
        H.remove_nodes_from([v] + nbrs)

    # Remaining graph has max degree < sqrt(n): greedy finishes it.
    greedy = nx.greedy_color(H, strategy="largest_first")
    for w, c in greedy.items():
        color[w] = next_color + c
    return color


# Build a genuine 3-colorable graph: a random tripartite graph.
import random
random.seed(7)
parts = [range(0, 12), range(12, 24), range(24, 36)]
G = nx.Graph()
G.add_nodes_from(range(36))
for i, A in enumerate(parts):
    for B in parts[i + 1:]:
        for a in A:
            for b in B:
                if random.random() < 0.4:
                    G.add_edge(a, b)

n = G.number_of_nodes()
coloring = approx_color_3colorable(G)
k = len(set(coloring.values()))
bound = 4 * math.ceil(math.sqrt(n))

assert all(coloring[u] != coloring[v] for u, v in G.edges())
assert k <= bound, (k, bound)
print(f"n = {n} vertices, graph is 3-colorable by construction.")
print(f"approximate algorithm used {k} colors")
print(f"theorem's guarantee: <= 4*ceil(sqrt(n)) = {bound}")
print(f"(true chromatic number is 3; the price of efficiency.)")
