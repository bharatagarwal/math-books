# uv run --with z3-solver --with networkx python \
#   code/bradfield/12-revision/04_z3_coloring.py
# CAPSTONE (logic + graph theory): encode graph k-coloring as a constraint
# problem and let z3 (a SAT/SMT solver, ch 4) decide it -- reproving the
# odd-cycle obstruction from ch 9 by machine.
import networkx as nx
from z3 import Int, Solver, sat, And

def k_colorable(graph, k):
    s = Solver()
    color = {v: Int(f"c_{v}") for v in graph.nodes()}
    for v in graph.nodes():
        s.add(And(color[v] >= 0, color[v] < k))   # k available colors
    for u, v in graph.edges():
        s.add(color[u] != color[v])               # adjacent => different
    return s.check() == sat

# Odd cycle C5: 3-colorable but NOT 2-colorable (i.e. not bipartite) -- the
# obstruction we found in the graph-theory chapter, now proved by the solver.
C5 = nx.cycle_graph(5)
assert k_colorable(C5, 3)
assert not k_colorable(C5, 2)

# The Petersen graph: a famous graph with chromatic number 3.
P = nx.petersen_graph()
assert k_colorable(P, 3)
assert not k_colorable(P, 2)

print("C5: 3-colorable yes, 2-colorable no (odd cycle => not bipartite)")
print("Petersen graph: chromatic number is 3 (3 yes, 2 no), per z3")
