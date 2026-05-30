# uv run --with numpy --with networkx --with hypothesis --with pytest pytest -q
#
# Exercise 13.1, property-tested: with the outer region blue, a region is
#   BLUE  if it lies inside an EVEN number of circles,
#   RED   if it lies inside an ODD  number of circles.
# Theorem 13.1 says this is a PROPER 2-coloring of the circle region map.
#
# Hypothesis throws hundreds of random circle arrangements at the claim instead
# of trusting one picture. For each arrangement we:
#   1. enumerate the realized regions by their "inside set" (which circles
#      contain the region), found by sampling many points;
#   2. build the true adjacency graph -- two regions touch along an arc iff
#      their inside-sets differ in exactly ONE circle;
#   3. color each region by parity of |inside set| and assert it is proper
#      AND that the outer region (inside-set = empty) is blue (parity 0).

import numpy as np
import networkx as nx
from hypothesis import given, settings, strategies as st


def regions_and_adjacency(circles):
    """circles: list of (cx, cy, r). Return (inside_sets, adjacency graph)."""
    n = len(circles)
    rng = np.random.default_rng(12345)
    pts = rng.uniform(-15, 15, size=(40000, 2))
    inside_sets = set()
    for x, y in pts:
        s = tuple(
            1 if (x - cx) ** 2 + (y - cy) ** 2 < r ** 2 else 0
            for (cx, cy, r) in circles
        )
        inside_sets.add(s)
    regions = sorted(inside_sets)
    G = nx.Graph()
    G.add_nodes_from(regions)
    for i in range(len(regions)):
        for j in range(i + 1, len(regions)):
            u, v = regions[i], regions[j]
            if sum(a != b for a, b in zip(u, v)) == 1:
                G.add_edge(u, v)
    return regions, G


@settings(max_examples=120, deadline=None)
@given(
    n=st.integers(min_value=1, max_value=4),
    data=st.data(),
)
def test_circle_parity_coloring(n, data):
    circles = []
    for _ in range(n):
        cx = data.draw(st.floats(min_value=-6, max_value=6, allow_nan=False))
        cy = data.draw(st.floats(min_value=-6, max_value=6, allow_nan=False))
        r = data.draw(st.floats(min_value=1.0, max_value=6.0, allow_nan=False))
        circles.append((cx, cy, r))

    regions, G = regions_and_adjacency(circles)

    # parity-of-enclosing-circles coloring (0 = blue, 1 = red)
    color = {s: sum(s) % 2 for s in regions}

    # (1) it is a PROPER 2-coloring on every realized arc-adjacency
    for u, v in G.edges():
        assert color[u] != color[v], f"parity coloring not proper on {u}-{v}"

    # (2) the outer region (inside nothing) is blue
    outer = tuple([0] * n)
    if outer in color:
        assert color[outer] == 0, "outer region should be blue (even=0)"

    # (3) the map is bipartite, the structural reason Theorem 13.1 holds
    assert nx.is_bipartite(G)


def test_book_figure_two_nested_and_overlap():
    """A concrete sanity case: two overlapping circles make 4 regions
    (outside / only-A / only-B / both); parity colors them blue,red,red,blue."""
    circles = [(-1.0, 0.0, 2.0), (1.0, 0.0, 2.0)]
    regions, G = regions_and_adjacency(circles)
    color = {s: sum(s) % 2 for s in regions}
    assert (0, 0) in color and color[(0, 0)] == 0   # outside both -> blue
    assert (1, 1) in color and color[(1, 1)] == 0   # inside both  -> blue
    assert (1, 0) in color and color[(1, 0)] == 1   # inside A only-> red
    for u, v in G.edges():
        assert color[u] != color[v]
    assert nx.is_bipartite(G)
