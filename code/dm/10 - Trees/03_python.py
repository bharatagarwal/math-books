# uv run --with networkx --with hypothesis --with pytest python -m pytest -q
#
# The Prufer code is a BIJECTION between labelled trees on n nodes and
# sequences of length n-2 over {0,...,n-1} (Section 10.4(d)). That bijection
# is the heart of the proof of Cayley's Theorem: #sequences = n^(n-2),
# so #trees = n^(n-2).
#
# We pin this down with property-based testing (hypothesis):
#   * to_prufer_sequence . from_prufer_sequence == identity on sequences
#     (every sequence decodes to a tree that re-encodes to the same sequence),
#   * from_prufer_sequence . to_prufer_sequence == identity on trees,
#   * the decoded object is always a genuine tree (connected, n-1 edges),
# and with an exhaustive check that decoding EVERY sequence of length n-2
# yields exactly n^(n-2) DISTINCT trees -- i.e. the map really is a bijection,
# reproducing the book's labelled-tree counts (16 for n=4, 125 for n=5).
import itertools

import networkx as nx
from hypothesis import given, settings
from hypothesis import strategies as st


def canon(G):
    """Canonical frozenset-of-edges so trees can go in a set."""
    return frozenset(frozenset(e) for e in G.edges())


# A Prufer sequence on n nodes: length n-2, entries in 0..n-1.
@st.composite
def prufer_sequences(draw, min_n=3, max_n=8):
    n = draw(st.integers(min_value=min_n, max_value=max_n))
    seq = draw(st.lists(st.integers(min_value=0, max_value=n - 1),
                        min_size=n - 2, max_size=n - 2))
    return n, seq


@settings(max_examples=400)
@given(prufer_sequences())
def test_sequence_roundtrip_and_is_tree(args):
    n, seq = args
    G = nx.from_prufer_sequence(seq)
    assert nx.is_tree(G)
    assert G.number_of_nodes() == n
    assert G.number_of_edges() == n - 1
    assert nx.to_prufer_sequence(G) == seq  # encode(decode(seq)) == seq


@settings(max_examples=200)
@given(st.integers(min_value=3, max_value=8))
def test_tree_roundtrip(n):
    # Decode a random sequence to get an arbitrary tree, then check
    # decode(encode(tree)) == tree.
    import random
    seq = [random.randrange(n) for _ in range(n - 2)]
    G = nx.from_prufer_sequence(seq)
    G2 = nx.from_prufer_sequence(nx.to_prufer_sequence(G))
    assert canon(G) == canon(G2)


def test_bijection_counts_match_cayley():
    # Exhaustive: decode every length-(n-2) sequence; the trees are all
    # distinct and number exactly n^(n-2) -- the book's 16 and 125.
    for n, expected in [(4, 16), (5, 125)]:
        trees = set()
        for seq in itertools.product(range(n), repeat=n - 2):
            trees.add(canon(nx.from_prufer_sequence(list(seq))))
        assert len(trees) == expected == n ** (n - 2)
