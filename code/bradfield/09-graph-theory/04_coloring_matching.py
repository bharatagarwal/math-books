# uv run --with scipy --with networkx python \
#   code/bradfield/09-graph-theory/04_coloring_matching.py
# Graph coloring (LL ch 13, scheduling/register allocation) and matching
# (LL ch 12, assignment) -- the two optimization problems that close the
# chapter, plus Konig's min-vertex-cover = max-matching equality.
import networkx as nx
from networkx.algorithms import bipartite


# A proper coloring gives adjacent vertices different colors. The chromatic
# number is the fewest colors needed. An EVEN cycle needs 2; an ODD cycle needs
# 3 -- the same odd-cycle obstruction as bipartiteness (LL ch 13).
def colors_used(g, **kw):
    c = nx.coloring.greedy_color(g, **kw)
    assert all(c[u] != c[v] for u, v in g.edges())  # proper?
    return len(set(c.values()))


assert colors_used(nx.cycle_graph(4)) == 2
assert colors_used(nx.cycle_graph(5), strategy="largest_first") == 3
# K_n needs n colors -- everyone is adjacent to everyone.
assert colors_used(nx.complete_graph(4)) == 4

# MATCHING: a set of edges with no shared endpoints (an assignment of workers
# to jobs). In a bipartite graph, the max matching of K_{2,3} has size
# min(2, 3) = 2.
B = nx.complete_bipartite_graph(2, 3)
m = nx.bipartite.maximum_matching(B, top_nodes=[0, 1])
matching_size = len(m) // 2          # dict stores both directions, halve it
assert matching_size == 2

# KONIG'S THEOREM (LL ch 12): in a bipartite graph, the size of a maximum
# matching equals the size of a minimum vertex cover. networkx derives the
# minimum cover from the matching; we check the two numbers agree.
cover = nx.bipartite.to_vertex_cover(B, m, top_nodes=[0, 1])
assert len(cover) == matching_size   # Konig: |min cover| = |max matching|

print("coloring: even cycle 2, odd cycle 3, K4 needs 4")
print("max matching in K(2,3) has size", matching_size,
      "= min vertex cover size", len(cover), "(Konig)")
