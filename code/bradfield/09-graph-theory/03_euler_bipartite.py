# uv run --with scipy --with networkx python \
#   code/bradfield/09-graph-theory/03_euler_bipartite.py
# Euler's bridges of Konigsberg, and bipartiteness -- two classic degree/cycle
# criteria, the original results that launched graph theory.
import networkx as nx

# EULER CIRCUIT (start and end at the same vertex, use every edge once) exists
# iff the graph is connected and EVERY vertex has even degree.
C4 = nx.cycle_graph(4)
assert nx.is_eulerian(C4)
assert all(d % 2 == 0 for _, d in C4.degree())

# EULER PATH (different endpoints) exists iff EXACTLY TWO vertices have odd
# degree. A path graph 0-1-2 has two odd-degree endpoints.
P = nx.path_graph(3)
odd = [v for v, d in P.degree() if d % 2 == 1]
assert len(odd) == 2
assert nx.has_eulerian_path(P) and not nx.is_eulerian(P)

# BIPARTITE (2-colorable) iff the graph has NO odd cycle. Even cycles are
# bipartite; odd cycles are the obstruction.
assert nx.is_bipartite(C4)                      # 4-cycle: bipartite
assert not nx.is_bipartite(nx.cycle_graph(5))   # 5-cycle: not bipartite

print("C4 is Eulerian (all even degrees);",
      "path 0-1-2 has an Euler path (2 odd vertices)")
print("even cycle bipartite:", nx.is_bipartite(C4),
      "  odd cycle bipartite:", nx.is_bipartite(nx.cycle_graph(5)))
