# uv run --with z3-solver python
#
# Theorem 9.1 via the book's second proof (Theorem 9.2 + parity), checked by an
# SMT solver rather than by hand. The book's argument:
#   sum of degrees = 2|E| is EVEN; dropping the even degrees leaves an even sum;
#   "but this is only possible if the number of odd degrees is even, since the
#    sum of an odd number of odd numbers is odd."
# We let Z3 search for a counterexample to that load-bearing parity claim.

from z3 import Int, Solver, Sum, Distinct, And, Implies, ForAll, Not, sat, unsat

# Part 1: a concrete bounded check. Pick k odd integers; if k is odd, can their
# sum ever be even? Ask Z3 for such a counterexample for k = 1, 3, 5, 7, 9.
print("Part 1: can an ODD number of odd integers sum to an EVEN value?")
for k in (1, 3, 5, 7, 9):
    xs = [Int(f"x_{k}_{i}") for i in range(k)]
    s = Solver()
    for x in xs:
        s.add(x % 2 == 1)            # each x_i is odd
    s.add(Sum(xs) % 2 == 0)          # their sum is even
    res = s.check()
    print(f"  k={k}: {res}  (unsat => impossible => sum is forced odd)")
    assert res == unsat

# Part 2: the contrapositive form actually used in the proof. Model the
# degrees of a small graph as integers and assert Theorem 9.2 (even degree
# sum). Then ask Z3: is it possible that the number of odd-degree nodes is
# ODD? It must be unsat.
print("\nPart 2: even degree-sum forces an EVEN count of odd-degree nodes")
for N in range(1, 8):
    d = [Int(f"d_{i}") for i in range(N)]          # the degree of each node
    odd = [Int(f"o_{i}") for i in range(N)]        # 1 if d_i is odd, else 0
    s = Solver()
    for i in range(N):
        s.add(d[i] >= 0)
        s.add(odd[i] == d[i] % 2)                  # parity indicator
    s.add(Sum(d) % 2 == 0)                         # Theorem 9.2: sum is even
    s.add(Sum(odd) % 2 == 1)                       # try: odd count is ODD
    res = s.check()
    print(f"  N={N}: {res}  (unsat => # odd-degree nodes must be even)")
    assert res == unsat

print("\nOK: Z3 confirms the parity step of Theorem 9.1 for all tested sizes.")
