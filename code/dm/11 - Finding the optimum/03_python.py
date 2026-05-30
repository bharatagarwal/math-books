# uv run --with hypothesis --with networkx --with pytest pytest -q
#
# Section 11.2: the "double-the-tree-and-shortcut" 2-approximation for TSP.
#
# The chapter proves a chain of inequalities for any costs satisfying the
# triangle inequality  c(ij) + c(jk) >= c(ik):
#
#   1. cost(cheapest spanning tree)  <  cost(cheapest tour)
#         "omit any edge of the cheapest tour to get a (path) spanning tree,
#          whose cost is >= the cheapest tree but < the tour".
#   2. walking around the tree uses every edge twice -> a closed walk of cost
#      exactly  2 * cost(tree).
#   3. shortcutting repeated towns can only shrink the walk (triangle ineq.),
#      giving a real tour with  cost(tour) <= 2 * cost(tree).
#
# Putting these together: the constructed tour costs at most twice the optimum.
# We verify all of this as PROPERTIES over many random Euclidean instances
# (Euclidean distance automatically satisfies the triangle inequality).
import itertools
import math

import networkx as nx
from hypothesis import given, settings, strategies as st


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def complete_graph(points):
    G = nx.Graph()
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=dist(points[i], points[j]))
    return G


def optimal_tour_cost(points):
    n = len(points)
    best = math.inf
    # Fix town 0 to avoid counting rotations of the same cycle.
    for perm in itertools.permutations(range(1, n)):
        order = (0,) + perm
        c = sum(dist(points[order[i]], points[order[(i + 1) % n]])
                for i in range(n))
        best = min(best, c)
    return best


def approx_tour(points):
    """Double-tree + shortcut tour exactly as the book describes."""
    G = complete_graph(points)
    T = nx.minimum_spanning_tree(G)
    tree_cost = T.size(weight="weight")

    # Walk around the tree (DFS preorder = the "planar code" walk of Fig 26),
    # then shortcut already-visited towns -> a Hamiltonian tour.
    walk = list(nx.dfs_preorder_nodes(T, source=0))
    order = walk + [walk[0]]
    tour_cost = sum(dist(points[order[i]], points[order[i + 1]])
                    for i in range(len(order) - 1))
    return tree_cost, tour_cost


# Distinct integer-coordinate towns, 3..7 of them.
@st.composite
def town_sets(draw):
    n = draw(st.integers(min_value=3, max_value=7))
    pts = draw(st.lists(
        st.tuples(st.integers(-15, 15), st.integers(-15, 15)),
        min_size=n, max_size=n, unique=True))
    return pts


@settings(max_examples=300, deadline=None)
@given(town_sets())
def test_triangle_inequality(points):
    # Euclidean costs satisfy c(ij)+c(jk) >= c(ik) for every triple.
    for i, j, k in itertools.permutations(range(len(points)), 3):
        assert dist(points[i], points[j]) + dist(points[j], points[k]) \
            >= dist(points[i], points[k]) - 1e-9


@settings(max_examples=300, deadline=None)
@given(town_sets())
def test_two_approximation_chain(points):
    tree_cost, tour_cost = approx_tour(points)
    opt = optimal_tour_cost(points)

    # (1) cheapest tree < cheapest tour  (tree_cost is the MST <= any tour's
    #     path-skeleton; strict unless degenerate, so use <=)
    assert tree_cost <= opt + 1e-9
    # (3) shortcut tour costs at most twice the tree
    assert tour_cost <= 2 * tree_cost + 1e-9
    # combined: the constructed tour is within a factor 2 of the optimum
    assert tour_cost <= 2 * opt + 1e-9
