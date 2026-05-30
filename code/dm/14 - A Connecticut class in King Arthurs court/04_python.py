# uv run --with networkx --with hypothesis --with pytest pytest -q
#
# The chapter's central claim, made into a property test.
#
# A "good characterization" (Frobenius' theorem) says that for a bipartite graph
# EXACTLY ONE of two easily-checkable certificates always exists:
#   (1) a PERFECT MATCHING               -- proves a perfect matching EXISTS;
#   (2) a Hall-violating set X (|N(X)| < |X|) -- proves one does NOT exist.
# Both certificates are verifiable in polynomial time, so BOTH "has a perfect
# matching" and its negation are NP-properties.  This is what let Merlin stay
# free on the marriage problem (unlike the Hamilton-cycle seating problem, whose
# non-existence has no known easy certificate).
#
# We let Hypothesis throw RANDOM bipartite graphs at this dichotomy and check
# that (a) exactly one certificate exists, and (b) whichever one networkx hands
# us actually verifies independently.

from itertools import combinations

import networkx as nx
from hypothesis import given, settings, strategies as st


def build_bigraph(left, right, edge_bits):
    G = nx.Graph()
    A = [f"a{i}" for i in range(left)]
    B = [f"b{j}" for j in range(right)]
    G.add_nodes_from(A, bipartite=0)
    G.add_nodes_from(B, bipartite=1)
    bit = 0
    for i in range(left):
        for j in range(right):
            use = edge_bits[bit % len(edge_bits)]
            if use and (i * 7 + j * 3 + bit) % 2 == 0:
                G.add_edge(f"a{i}", f"b{j}")
            bit += 1
    return G, A, B


def find_hall_violator(G, A):
    for r in range(1, len(A) + 1):
        for X in combinations(A, r):
            nbrs = set()
            for x in X:
                nbrs.update(G.neighbors(x))
            if len(nbrs) < len(X):
                return set(X)
    return None


@settings(max_examples=200, deadline=None)
@given(
    left=st.integers(min_value=1, max_value=5),
    right=st.integers(min_value=1, max_value=5),
    edge_bits=st.lists(st.booleans(), min_size=4, max_size=12),
)
def test_good_characterization(left, right, edge_bits):
    G, A, B = build_bigraph(left, right, edge_bits)

    if G.number_of_edges():
        M = nx.bipartite.hopcroft_karp_matching(G, top_nodes=A)
    else:
        M = {}
    # A perfect matching here means every node of the SMALLER side A is matched.
    a_matched = sum(1 for u in M if u in A)
    has_perfect_for_A = (a_matched == left)

    violator = find_hall_violator(G, A)

    # Frobenius dichotomy: A is fully matchable  <=>  no Hall violator on A.
    assert has_perfect_for_A == (violator is None)

    if has_perfect_for_A:
        # Certificate (1): verify the matching uses real edges, covers all of A,
        # and matches distinct partners (the easy NP check).
        used_b = set()
        for u in A:
            v = M[u]
            assert G.has_edge(u, v)
            assert v not in used_b
            used_b.add(v)
    else:
        # Certificate (2): verify the Hall witness independently.
        nbrs = set()
        for x in violator:
            nbrs.update(G.neighbors(x))
        assert len(nbrs) < len(violator)
