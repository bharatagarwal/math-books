# uv run --with numpy --with networkx python
#
# Exercise 13.2: the regions cut out by n straight lines are 2-colorable, and
# we can name a region's color WITHOUT coloring the whole picture.
#
# Color rule (the line analogue of Exercise 13.1's "parity of
# enclosing circles"): each line a*x + b*y = c splits the plane into
# side(>0) and side(<0). Give a region the sign vector s in {+,-}^n
# recording which side of each line it is on.
# Define its color = parity of (number of '+' signs). Crossing exactly one line
# flips one sign, hence flips the parity -> neighboring regions ALWAYS differ.
#
# We verify this concretely: drop n random lines, enumerate the actual regions
# by their sign vectors, build the true adjacency graph (two regions are
# neighbors iff their sign vectors differ in exactly ONE coordinate -- they meet
# along that one line), then check the parity coloring is proper on every edge.

import itertools
import numpy as np
import networkx as nx

def line_arrangement_demo(lines, seed_label):
    n = len(lines)

    # Sample many points; each gets a sign vector (which side of each line).
    rng = np.random.default_rng(0)
    pts = rng.uniform(-10, 10, size=(20000, 2))
    sign_vectors = set()
    for x, y in pts:
        sv = tuple(1 if a * x + b * y - c > 0 else 0 for (a, b, c) in lines)
        sign_vectors.add(sv)

    regions = sorted(sign_vectors)

    # Adjacency: two realized regions are neighbors iff their sign vectors
    # differ in exactly one line (they sit on opposite sides of just that line).
    G = nx.Graph()
    G.add_nodes_from(regions)
    for u, v in itertools.combinations(regions, 2):
        if sum(a != b for a, b in zip(u, v)) == 1:
            G.add_edge(u, v)

    # The parity coloring.
    color = {sv: sum(sv) % 2 for sv in regions}

    # Check it is PROPER on every realized adjacency.
    bad = [(u, v) for u, v in G.edges() if color[u] == color[v]]

    print(f"[{seed_label}] n={n} lines -> {len(regions)} regions sampled, "
          f"{G.number_of_edges()} adjacencies")
    print(f"    parity coloring proper on all edges: {len(bad) == 0}")
    print(f"    region adjacency graph bipartite:    {nx.is_bipartite(G)}")
    print(f"    colors used: {sorted(set(color.values()))}")
    assert not bad, f"parity rule failed on {bad}"
    assert nx.is_bipartite(G)
    return regions, color

# Three random "generic" line arrangements
# (the kind Figure 43-style maps avoid).
arrangements = {
    "A": [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 1.0)],          # 3 lines
    "B": [(1.0, 2.0, 1.0), (2.0, -1.0, 0.5), (-1.0, 1.0, -2.0),
          (0.0, 1.0, 3.0)],                                            # 4 lines
    "C": [(1.0, 0.3, 0.0), (0.2, 1.0, 1.0), (1.0, -1.0, -0.4),
          (-0.5, 1.0, 2.0), (1.0, 1.0, -1.5)],                         # 5 lines
}

for label, lines in arrangements.items():
    line_arrangement_demo(lines, label)

print("\nExercise 13.2 confirmed: 'color = parity of the + signs' is a")
print("proper 2-coloring of every line arrangement -- crossing one line")
print("flips one sign, so neighbors differ. The map is bipartite,")
print("exactly as Theorem 13.1 needs.")
