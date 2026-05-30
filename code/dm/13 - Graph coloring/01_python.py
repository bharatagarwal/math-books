# uv run --with networkx python
#
# Section 13: proper coloring and the chromatic number chi(G).
# A proper coloring assigns colors to vertices so adjacent vertices differ;
# chi(G) is the fewest colors any proper coloring needs.
#
# The chapter's "easy 2-color case" (Theorem 13.1) says the region map of n
# circles is always 2-colorable. The deep reason: that adjacency graph has no
# odd cycle, i.e. it is BIPARTITE, and a graph is 2-colorable iff bipartite.
# Here we contrast a bipartite "region" graph (chi = 2) with an odd cycle
# C_5 (chi = 3) using networkx's greedy_color across several strategies.

import networkx as nx

def colors_used(G, strategy):
    coloring = nx.greedy_color(G, strategy=strategy)
    return coloring, (1 + max(coloring.values()) if coloring else 0)

strategies = ["largest_first", "smallest_last",
              "saturation_largest_first", "random_sequential"]

# (1) A bipartite region-style graph: even cycle C_6 (alternating regions).
#     No odd cycle => 2-colorable, exactly the circle/line situation.
C6 = nx.cycle_graph(6)
print("C_6 (even cycle, bipartite -> the '2-color' situation):")
print(f"  is_bipartite = {nx.is_bipartite(C6)}")
for s in strategies:
    _, k = colors_used(C6, s)
    print(f"  greedy[{s:<26}] used {k} colors")

# (2) An odd cycle C_5: NOT bipartite, so 2 colors are impossible.
C5 = nx.cycle_graph(5)
print("\nC_5 (odd cycle, NOT bipartite -> needs 3):")
print(f"  is_bipartite = {nx.is_bipartite(C5)}")
for s in strategies:
    _, k = colors_used(C5, s)
    print(f"  greedy[{s:<26}] used {k} colors")

# greedy_color is only an UPPER bound on chi (it can overshoot). The exact
# value comes from z3 in 02_python.py. But the bipartite/not-bipartite split
# already nails the 2-vs-3 boundary the chapter cares about.
print("\nTheorem 13.1 in graph terms: a circle/line region map is bipartite,")
print("hence 2-colorable. The moment an odd cycle appears, you need 3.")
