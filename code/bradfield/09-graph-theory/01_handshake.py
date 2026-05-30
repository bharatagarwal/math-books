# uv run --with scipy --with networkx python \
#   code/bradfield/09-graph-theory/01_handshake.py
# Degrees and the handshake lemma -- the first theorem of graph theory.
import networkx as nx

G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 0)])
degs = dict(G.degree())

# Handshake lemma: every edge contributes 2 to the total degree, so
# sum of degrees = 2 * |E|. (At a party, the handshakes counted per person
# double-count each handshake.)
assert sum(degs.values()) == 2 * G.number_of_edges()

# Immediate corollary: the number of ODD-degree vertices is even. (You cannot
# have an odd number of people who each shook an odd number of hands.)
odd = [v for v, d in degs.items() if d % 2 == 1]
assert len(odd) % 2 == 0

# The complete graph K_n: every pair joined, so C(n,2) edges and degree n-1.
K5 = nx.complete_graph(5)
assert K5.number_of_edges() == 5 * 4 // 2 == 10
assert all(d == 4 for _, d in K5.degree())

print("sum of degrees =", sum(degs.values()), "= 2|E| =",
      2 * G.number_of_edges())
print("odd-degree vertices:", odd, "(an even number, as the lemma forces)")
