# uv run --with scipy --with networkx python \
#   code/bradfield/09-graph-theory/06_prom_hall.py
# INTUITION (LL ch 12): the prom-dancing problem and Hall's condition.
# DISCOVER why a perfect matching must exist by (a) watching a d-regular
# bipartite graph always match everyone as d grows, and (b) seeing that a
# matching fails EXACTLY when some k left nodes touch fewer than k right nodes.
import itertools
import networkx as nx
from networkx.algorithms import bipartite


def regular_bipartite(side, d):
    # A clean d-regular bipartite graph: left node i joins right nodes
    # i, i+1, ..., i+d-1 (mod side). Every node has degree exactly d, and
    # the "diagonal" {i -- side+i} is an obvious perfect matching.
    g = nx.Graph()
    left = list(range(side))
    right = list(range(side, 2 * side))
    g.add_nodes_from(left, bipartite=0)
    g.add_nodes_from(right, bipartite=1)
    for i in left:
        for k in range(d):
            g.add_edge(i, side + (i + k) % side)
    return g, left


# (a) As the common degree d grows, a d-regular bipartite "prom" still pairs
# everyone off -- Theorem 12.1 (LL ch 12). Watch the matching cover all nodes.
print("d-regular bipartite proms (LL Thm 12.1): everyone can dance")
for d in (1, 2, 3, 5):
    g, left = regular_bipartite(side=8, d=d)
    assert all(deg == d for _, deg in g.degree())   # genuinely d-regular
    m = bipartite.maximum_matching(g, top_nodes=left)
    matched = len(m) // 2
    print(f"  d={d}: |E|={g.number_of_edges():3d}  matched {matched}/8 pairs")
    assert matched == 8                              # perfect matching exists


# (b) Hall's condition (the Marriage Theorem, LL Thm 12.2): a perfect matching
# exists IFF every set S of k left nodes has >= k neighbors on the right.
# Build the tribes-and-tortoises graph (Figure 32): tribe A has 2 choices,
# tribe D has 4, etc. Check Hall over ALL 2^6 subsets, then find the matching.
tribes = ["A", "B", "C", "D", "E", "F"]
totems = ["t1", "t2", "t3", "t4", "t5", "t6"]
choices = {
    "A": ["t1", "t2"],
    "B": ["t2", "t3"],
    "C": ["t3", "t4"],
    "D": ["t1", "t4", "t5", "t6"],
    "E": ["t5", "t6"],
    "F": ["t1", "t6"],
}
H = nx.Graph()
H.add_nodes_from(tribes, bipartite=0)
H.add_nodes_from(totems, bipartite=1)
for tr, ts in choices.items():
    for t in ts:
        H.add_edge(tr, t)


def neighbors_of(subset):
    out = set()
    for tr in subset:
        out |= set(choices[tr])
    return out


hall_ok = True
for r in range(len(tribes) + 1):
    for S in itertools.combinations(tribes, r):
        if len(neighbors_of(S)) < len(S):
            hall_ok = False
print("Hall's condition over all 2^6 subsets:", hall_ok)
assert hall_ok

m = bipartite.maximum_matching(H, top_nodes=tribes)
assignment = {tr: m[tr] for tr in tribes}
print("totem assignment:", assignment)
assert len(set(assignment.values())) == 6     # all six totems distinct

# Now BREAK it (exercise 12.2(b)): make three tribes share only two totems.
# Then some k=3 left nodes have only 2 neighbors -> Hall fails -> no matching.
bad_choices = dict(choices)
bad_choices["A"] = ["t1", "t2"]
bad_choices["B"] = ["t1", "t2"]
bad_choices["C"] = ["t1", "t2"]               # A,B,C all confined to {t1,t2}
bad = nx.Graph()
bad.add_nodes_from(tribes, bipartite=0)
bad.add_nodes_from(totems, bipartite=1)
for tr, ts in bad_choices.items():
    for t in ts:
        bad.add_edge(tr, t)
nb = set(bad_choices["A"]) | set(bad_choices["B"]) | set(bad_choices["C"])
print("violating S={A,B,C}: |neighbors| =", len(nb), "< |S| = 3")
assert len(nb) == 2
bad_m = bipartite.maximum_matching(bad, top_nodes=tribes)
print("max matching size when Hall fails:", len(bad_m) // 2, "(< 6)")
assert len(bad_m) // 2 < 6                     # no perfect matching
