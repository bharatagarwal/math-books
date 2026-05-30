# uv run --with z3-solver python
#
# A perfect matching as a Boolean constraint problem (Sections 12.3-12.4).
# Section 12.4 notes that brute force over all pairings is hopeless
# (150! ~ 10^263). Instead we hand the EXISTENCE question to the Z3 SMT
# solver as constraints: a boolean x[a,b] per edge meaning "a is matched to b",
# with "exactly one" per node on each side. Z3 finds a perfect matching if
# one exists (SAT) and PROVES none exists otherwise (UNSAT).
#
# We test two graphs from the chapter's logic:
#   * a "good" graph (Hall's condition holds)  -> SAT, real matching returned
#   * a graph violating Hall (exercise 12.2b: positive degree, but two left
#     nodes share the SAME single neighbour) -> UNSAT, no perfect matching.

from z3 import Bool, Solver, PbEq, Implies, Or, sat


def perfect_matching(A, B, edges):
    """Return a perfect matching dict via Z3, or None if provably impossible."""
    x = {(a, b): Bool(f"x_{a}_{b}") for (a, b) in edges}
    s = Solver()
    # Each left node a is matched to exactly one neighbour.
    # (Or() is the empty disjunction == False: an isolated node makes
    # the whole problem UNSAT, as it cannot be matched.)
    for a in A:
        inc = [x[(a, b)] for b in B if (a, b) in x]
        s.add(PbEq([(lit, 1) for lit in inc], 1) if inc else Or())
    # Each right node b is matched to exactly one neighbour.
    for b in B:
        inc = [x[(a, b)] for a in A if (a, b) in x]
        s.add(PbEq([(lit, 1) for lit in inc], 1) if inc else Or())
    if s.check() == sat:
        m = s.model()
        return {a: b for (a, b) in edges if m.evaluate(x[(a, b)], True)}
    return None


# --- Good graph: 3+3, Hall holds (a path-like cover exists) ---
A1, B1 = [0, 1, 2], [0, 1, 2]
edges1 = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 0)]
m1 = perfect_matching(A1, B1, edges1)
print("good graph -> perfect matching:", m1)
assert m1 is not None and len(set(m1.values())) == 3

# --- Bad graph (exercise 12.2b): every node has positive degree, BUT
# left nodes 0 and 1 are BOTH connected only to right node 0. Two tribes,
# one tortoise: Hall fails, so no perfect matching can exist. ---
A2, B2 = [0, 1, 2], [0, 1, 2]
edges2 = [(0, 0), (1, 0), (2, 1), (2, 2)]
m2 = perfect_matching(A2, B2, edges2)
print("Hall-violating graph -> perfect matching:", m2)
assert m2 is None, "Z3 must PROVE no perfect matching exists (UNSAT)"

print("Z3 confirms the Marriage Theorem operationally: SAT exactly when a")
print("perfect matching exists, UNSAT (a proof of impossibility) when Hall")
print("fails.")
