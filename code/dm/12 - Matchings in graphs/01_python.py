# uv run --with networkx python
#
# The dancing problem (Section 12.1, Theorem 12.1).
# 300 students: 150 boys (A), 150 girls (B); every node has degree exactly 50.
# The book claims they can ALL dance simultaneously -- i.e. the bipartite graph
# has a PERFECT MATCHING (Theorem 12.1: a d-regular bipartite graph, d >= 1,
# always has one). We build a concrete 50-regular bipartite graph on 150+150
# nodes, reproduce the book's edge count (150 * 50 = 7500), then run
# Hopcroft-Karp maximum bipartite matching and confirm it is perfect.

import networkx as nx

n = 150   # |A| = |B| = 300 / 2  (the book's numbers)
d = 50    # every student knows exactly 50 of the opposite group

# A clean way to get a d-regular bipartite graph: boy i knows girls
# i, i+1, ..., i+49 (indices mod 150). This is a "circulant" bipartite graph;
# every boy has degree 50 and, by symmetry, every girl does too.
A = [("boy", i) for i in range(n)]
B = [("girl", j) for j in range(n)]

G = nx.Graph()
G.add_nodes_from(A, bipartite=0)
G.add_nodes_from(B, bipartite=1)
for i in range(n):
    for k in range(d):
        G.add_edge(("boy", i), ("girl", (i + k) % n))

# Reproduce the book's bookkeeping exactly.
degs = {deg for _, deg in G.degree()}
print("distinct degrees in the graph:", degs)            # {50}
print("number of edges:", G.number_of_edges())           # 150 * 50 = 7500
assert degs == {d}
assert G.number_of_edges() == n * d == 7500

# Hopcroft-Karp maximum matching on the bipartite graph.
matching = nx.bipartite.hopcroft_karp_matching(G, top_nodes=A)
# hopcroft_karp_matching returns each matched node mapped to its partner
# (both directions), so a perfect matching covers all 300 nodes.
matched_nodes = len(matching)
pairs = matched_nodes // 2
print("students matched:", matched_nodes, "/ 300")
print("dancing pairs:", pairs)

# Verify it is a genuine matching (no shared endpoints) and PERFECT.
seen = set()
for u, v in matching.items():
    assert G.has_edge(u, v), "matched pair must be an actual acquaintance edge"
    seen.add(u)
assert seen == set(G.nodes()), "every node is matched -> perfect matching"
assert pairs == n == 150

print("Theorem 12.1 confirmed: the 50-regular bipartite graph on 300 nodes")
print("has a PERFECT MATCHING -- all 150 pairs can dance at once.")
