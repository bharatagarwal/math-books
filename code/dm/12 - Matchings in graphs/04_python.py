# uv run --with z3-solver python
#
# Hamiltonian cycles (Section 12.5).
# The book contrasts matchings with Hamiltonian cycles: "in a perfect matching
# every node belongs to exactly ONE edge; in a Hamiltonian cycle every node
# belongs to exactly TWO edges." No efficient test is known, so we model the
# search as constraints and let Z3 do the work.
#
# Encoding: pos[v] in {0..n-1} is the position of node v on the cycle; all
# positions distinct (Distinct), and consecutive positions (wrapping around)
# must be joined by an edge. A satisfying assignment IS a Hamiltonian cycle;
# UNSAT is a proof that none exists.

from z3 import Int, Distinct, Solver, Or, And, sat


def hamiltonian_cycle(n, edges):
    E = set(map(frozenset, edges))
    pos = [Int(f"pos_{v}") for v in range(n)]
    s = Solver()
    for p in pos:
        s.add(p >= 0, p < n)
    s.add(Distinct(pos))
    s.add(pos[0] == 0)  # fix the starting node to break rotational symmetry
    # For every ORDERED pair (u, v), if they are cyclically adjacent on the
    # tour (pos differ by 1 mod n) then {u, v} must be an edge of the graph.
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            adjacent = Or(
                pos[v] == pos[u] + 1,
                And(pos[u] == n - 1, pos[v] == 0),
            )
            if frozenset((u, v)) not in E:
                s.add(adjacent == False)  # non-edges may not be consecutive
    if s.check() == sat:
        m = s.model()
        order = sorted(range(n), key=lambda v: m[pos[v]].as_long())
        return order + [order[0]]
    return None


# (1) The 5-cycle C5 plus a chord -- clearly Hamiltonian (the outer
# 5-cycle 0-1-2-3-4-0 already visits every node).
n1 = 5
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)]
cyc1 = hamiltonian_cycle(n1, edges1)
print("C5(+chord) Hamiltonian cycle:", cyc1)
assert cyc1 is not None and len(set(cyc1[:-1])) == n1
for a, b in zip(cyc1, cyc1[1:]):
    assert frozenset((a, b)) in set(map(frozenset, edges1))

# (2) A bipartite graph with UNEQUAL sides cannot have a Hamiltonian cycle:
# a cycle alternates sides, so a Ham. cycle forces |A| = |B|. Here |A|=3,|B|=2.
# (Same flavor as why Theorem 12.2 needs |A| = |B|.) Z3 should report UNSAT.
n2 = 5  # left = {0,1,2}, right = {3,4}
edges2 = [(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]
cyc2 = hamiltonian_cycle(n2, edges2)
print("unbalanced bipartite (|A|=3,|B|=2) Hamiltonian cycle:", cyc2)
assert cyc2 is None, "no Hamiltonian cycle when the two sides differ in size"

print("Z3 found a Hamiltonian cycle in the first graph and PROVED none exists")
print("in the unbalanced bipartite graph -- matching the book's degree-2")
print("picture.")
