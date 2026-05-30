# uv run --with z3-solver python
#
# The EXACT chromatic number chi(G) as a satisfiability problem.
# Greedy coloring (01_python.py) only gives an upper bound. To pin down chi
# exactly we ask z3: "is there a proper coloring with k colors?" for growing k.
# The smallest k that is SAT is chi(G). To be sure chi > k-1 we also show the
# (k-1)-color attempt is UNSAT -- a machine-checked proof of the lower bound.
#
# We reproduce the 2-vs-3 boundary the chapter hinges on:
#   - even cycle C_6  (bipartite region map, Theorem 13.1) -> chi = 2
#   - odd cycle  C_5                                        -> chi = 3
#   - complete graph K_4 (every country borders every other) -> chi = 4

from z3 import Int, And, Or, Distinct, Solver, sat

def edges_cycle(n):
    return [(i, (i + 1) % n) for i in range(n)]

def edges_complete(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]

def k_colorable(n_vertices, edges, k):
    """Is the graph properly colorable with k colors? Return (sat?, model)."""
    c = [Int(f"c_{i}") for i in range(n_vertices)]
    s = Solver()
    for v in c:                                  # each color in {0,...,k-1}
        s.add(And(v >= 0, v < k))
    for (u, v) in edges:                         # adjacent vertices differ
        s.add(c[u] != c[v])
    if s.check() == sat:
        m = s.model()
        return True, [m[ci].as_long() for ci in c]
    return False, None

def chromatic_number(name, n, edges):
    k = 1
    while True:
        ok, model = k_colorable(n, edges, k)
        if ok:
            # prove the lower bound: k-1 colors are impossible (unless k==1)
            lower_unsat = (k == 1) or (not k_colorable(n, edges, k - 1)[0])
            print(f"{name}: chi = {k}  "
                  f"({k} SAT, {k-1} UNSAT = {lower_unsat})  coloring={model}")
            return k
        k += 1

chromatic_number("C_6 (bipartite region map)", 6, edges_cycle(6))
chromatic_number("C_5 (odd cycle)          ", 5, edges_cycle(5))
chromatic_number("K_4 (mutual borders)     ", 4, edges_complete(4))

# Sanity checks tying the numbers to the chapter's claims.
assert k_colorable(6, edges_cycle(6), 2)[0]            # C_6 IS 2-colorable
assert not k_colorable(5, edges_cycle(5), 2)[0]        # C_5 is NOT 2-colorable
assert not k_colorable(4, edges_complete(4), 3)[0]     # K_4 is NOT 3-colorable
print("\nAll lower-bound proofs (UNSAT for k-1) checked:")
print("  chi(C_6)=2, chi(C_5)=3, chi(K_4)=4.")
