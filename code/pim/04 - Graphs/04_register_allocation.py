# uv run --with networkx --with scipy python \
#   "code/pim/04 - Graphs/04_register_allocation.py"
"""Section 6.3: register allocation as graph coloring.

We take Kun's "almost-assembly" snippet, compute liveness by a
backward pass (a variable is live at a statement if its value is
read later before being overwritten), build the interference graph
-- two variables interfere if they are ever live at the same time
-- and color it.  The number of colors is the number of physical
registers needed.
"""
import networkx as nx

# (defs, uses) per statement, in program order, from the snippet:
#   $41 = $41 - 1
#   $40 = $40 + $42
#   $42 = $41 - $42
#   BranchIfZero $41 ...     (reads $41)
#   $43 = $41 + $40
program = [
    ({"41"}, {"41"}),         # $41 = $41 - 1
    ({"40"}, {"40", "42"}),   # $40 = $40 + $42
    ({"42"}, {"41", "42"}),   # $42 = $41 - $42
    (set(),  {"41"}),         # BranchIfZero $41
    ({"43"}, {"41", "40"}),   # $43 = $41 + $40
]


def liveness(program):
    """live_out[i]: variables live after statement i (backward pass)."""
    n = len(program)
    live_out = [set() for _ in range(n)]
    live = set()
    for i in range(n - 1, -1, -1):
        defs, uses = program[i]
        live_out[i] = set(live)
        live = (live - defs) | uses   # gen/kill dataflow equation
    return live_out


def interference_graph(program):
    G = nx.Graph()
    for defs, uses in program:
        G.add_nodes_from(defs | uses)
    # Two vars interfere if simultaneously live (here: live together
    # at some statement's def/use sets or its live-out set).
    live_out = liveness(program)
    for i, (defs, uses) in enumerate(program):
        simultaneous = defs | uses | live_out[i]
        for a in simultaneous:
            for b in simultaneous:
                if a < b:
                    G.add_edge(a, b)
    return G


G = interference_graph(program)
print("Interference edges (variables that cannot share a register):")
for u, v in sorted(G.edges()):
    print(f"  ${u} -- ${v}")

# Kun notes $41 and $42 must differ; verify the edge is present.
assert G.has_edge("41", "42"), "$41 and $42 must interfere"

coloring = nx.greedy_color(G, strategy="largest_first")
num_registers = len(set(coloring.values()))
assert all(coloring[u] != coloring[v] for u, v in G.edges())
print(f"\nGreedy coloring -> {num_registers} physical registers:")
for var in sorted(coloring):
    print(f"  ${var} -> register R{coloring[var]}")
