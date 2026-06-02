# uv run --with networkx --with scipy python \
#   "code/pim/04 - Graphs/02_greedy_bound.py"
"""Proposition 6.4: the greedy algorithm uses at most d + 1 colors,
where d is the largest degree.

We implement the exact greedy coloring from Kun's proof: fix an
order of the vertices, and give each vertex the smallest color not
used by an already-colored neighbor.  Then we confirm the bound,
and show it is *loose* on the star graph (d = n-1 but chi = 2).
"""
import networkx as nx


def greedy_coloring(G, order):
    color = {}
    for v in order:
        used = {color[u] for u in G.neighbors(v) if u in color}
        c = 0
        while c in used:          # first color not used by a neighbor
            c += 1
        color[v] = c
    return color


def is_proper(G, color):
    return all(color[u] != color[v] for u, v in G.edges())


def max_degree(G):
    return max((d for _, d in G.degree()), default=0)


for name, G in [("Petersen", nx.petersen_graph()),
                ("K5", nx.complete_graph(5)),
                ("star S9", nx.star_graph(9))]:
    d = max_degree(G)
    color = greedy_coloring(G, list(G.nodes()))
    k = len(set(color.values()))
    assert is_proper(G, color)
    assert k <= d + 1, (name, k, d)
    print(f"{name:>9}: max deg d={d}, greedy used {k} colors "
          f"(bound d+1 = {d + 1})")

# The bound is tight for K5 (k = d+1 = 5) but useless for the star:
star = nx.star_graph(9)
star_color = greedy_coloring(star, list(star.nodes()))
print(f"\nStar S9: greedy={len(set(star_color.values()))} colors, "
      f"true chi=2, yet d+1={max_degree(star) + 1}.")
print("The d+1 guarantee can be arbitrarily loose.")
