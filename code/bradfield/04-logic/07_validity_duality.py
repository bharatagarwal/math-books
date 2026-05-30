# uv run python code/bradfield/04-logic/07_validity_duality.py
"""Make the validity / satisfiability duality concrete (MCS 3.3).

MCS 3.3 states: a formula P is VALID iff its negation NOT(P) is
UNSATISFIABLE.  Before handing the job to a SAT solver, let's watch the
duality directly over a full truth table -- count how many of the 2^n
assignments satisfy P, and confirm:

  * P is valid       <=>  every assignment satisfies P  <=> NOT(P) has 0 models
  * P is satisfiable <=>  at least one assignment satisfies P
  * P is unsat       <=>  no assignment satisfies P      <=> NOT(P) is valid

We tabulate the chain syllogism, excluded middle, a contradiction, and
the MCS 3.5 SAT example, then assert the duality holds in every case.
"""
from itertools import product


def truth_table(fn, n):
    """Return list of (assignment, value) over all 2^n assignments."""
    return [(a, fn(*a)) for a in product([True, False], repeat=n)]


def models(fn, n):
    return sum(1 for _, v in truth_table(fn, n) if v)


def is_valid(fn, n):
    return models(fn, n) == 2 ** n


def is_sat(fn, n):
    return models(fn, n) > 0


# Chain syllogism: ((P->Q) & (Q->R)) -> (P->R)
def imp(p, q):
    return (not p) or q


def chain(P, Q, R):
    return imp(imp(P, Q) and imp(Q, R), imp(P, R))


def excluded_middle(P):
    return P or (not P)


def contradiction(P):
    return P and (not P)


def mcs_35(P, Q, R):
    return ((P or Q or R) and (not (P and Q))
            and (not (P and R)) and (not (R and Q)))


def report(name, fn, n):
    m = models(fn, n)
    neg_m = 2 ** n - m  # models of NOT(fn)
    print(f"{name}: {m}/{2**n} assignments true | "
          f"valid={is_valid(fn, n)} sat={is_sat(fn, n)}")
    # The duality: P valid  <=>  NOT(P) unsatisfiable (0 models).
    assert is_valid(fn, n) == (neg_m == 0)
    # And: P satisfiable  <=>  NOT(P) not valid.
    assert is_sat(fn, n) == (neg_m < 2 ** n)


def main():
    report("chain syllogism", chain, 3)
    report("excluded middle", excluded_middle, 1)
    report("contradiction  ", contradiction, 1)
    report("MCS 3.5 formula", mcs_35, 3)
    print("\nduality verified: valid(P) == unsat(NOT P) in every case.")


main()
