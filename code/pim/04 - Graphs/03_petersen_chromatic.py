# uv run --with networkx --with scipy python \
#   "code/pim/04 - Graphs/03_petersen_chromatic.py"
"""Definition 6.3: the chromatic number chi(G) is the smallest k
for which G is k-colorable.

We compute chi by brute force -- try every assignment of k colors
to the vertices for k = 1, 2, 3, ... and stop at the first k that
admits a proper coloring.  This confirms Kun's claim that the
Petersen graph is 3-colorable but not 2-colorable, so chi = 3.
"""
from itertools import product
import networkx as nx


def is_k_colorable(G, k):
    nodes = list(G.nodes())
    edges = list(G.edges())
    for assignment in product(range(k), repeat=len(nodes)):
        color = dict(zip(nodes, assignment))
        if all(color[u] != color[v] for u, v in edges):
            return color
    return None


def chromatic_number(G):
    k = 1
    while is_k_colorable(G, k) is None:
        k += 1
    return k


G = nx.petersen_graph()
assert is_k_colorable(G, 2) is None, "Petersen should NOT be 2-colorable"
three = is_k_colorable(G, 3)
assert three is not None, "Petersen should be 3-colorable"

print("Petersen graph:")
print(f"  2-colorable? {is_k_colorable(G, 2) is not None}")
print(f"  3-colorable? {is_k_colorable(G, 3) is not None}")
print(f"  chromatic number chi(G) = {chromatic_number(G)}")
print(f"  a valid 3-coloring: {three}")
