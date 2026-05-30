# uv run --with networkx --with hypothesis --with pytest pytest -q
#
# Property-based test of Theorem 9.1 ("the handshake lemma"):
#   In EVERY graph, the number of nodes with odd degree is even.
# Instead of one example, Hypothesis throws hundreds of random graphs at it
# via nx.gnp_random_graph(n, p) with n and p drawn from wide ranges.
# We also confirm Theorem 9.2 (sum(deg) = 2|E|) on the same random graphs,
# since Theorem 9.1 is a corollary of it.

import networkx as nx
from hypothesis import given, settings, strategies as st


@settings(max_examples=400)
@given(
    n=st.integers(min_value=0, max_value=40),
    p=st.floats(min_value=0.0, max_value=1.0),
    seed=st.integers(min_value=0, max_value=10_000),
)
def test_handshake_lemma(n, p, seed):
    G = nx.gnp_random_graph(n, p, seed=seed)
    degrees = [d for _, d in G.degree()]

    # Theorem 9.2: sum of degrees is twice the number of edges.
    assert sum(degrees) == 2 * G.number_of_edges()

    # Theorem 9.1: the count of odd-degree nodes is even.
    odd_count = sum(1 for d in degrees if d % 2 == 1)
    assert odd_count % 2 == 0


@settings(max_examples=200)
@given(
    edges=st.lists(
        st.tuples(st.integers(0, 12), st.integers(0, 12)),
        max_size=40,
    )
)
def test_handshake_on_arbitrary_edge_lists(edges):
    # Build a graph one edge at a time (mirrors the book's inductive proof:
    # each added edge flips the parity at its two endpoints).
    G = nx.Graph()
    G.add_nodes_from(range(13))
    G.add_edges_from((u, v) for u, v in edges if u != v)
    odd_count = sum(1 for _, d in G.degree() if d % 2 == 1)
    assert odd_count % 2 == 0
    assert sum(d for _, d in G.degree()) == 2 * G.number_of_edges()
