# uv run --with z3-solver python code/bradfield/04-logic/02_z3_validity.py
# Validity by SAT (MCS 3.3): a formula is valid iff its NEGATION is
# unsatisfiable. The same solver decides satisfiability directly.
from z3 import Bools, Solver, Implies, And, Or, Not, unsat, sat


p, q, r = Bools("p q r")


def is_valid(formula):
    # Search for a counterexample (a model of the negation). None => valid.
    s = Solver()
    s.add(Not(formula))
    return s.check() == unsat


def is_satisfiable(formula):
    s = Solver()
    s.add(formula)
    return s.check() == sat


def counterexample(formula):
    s = Solver()
    s.add(Not(formula))
    return s.model() if s.check() == sat else None


# Distributivity of AND over OR (MCS Theorem 3.4.1) -- valid.
distrib = And(p, Or(q, r)) == Or(And(p, q), And(p, r))
assert is_valid(distrib)

# De Morgan for AND (MCS 3.4): NOT(p AND q) == (NOT p OR NOT q) -- valid.
de_morgan = Not(And(p, q)) == Or(Not(p), Not(q))
assert is_valid(de_morgan)

# Hypothetical syllogism: (p->q) & (q->r)  =>  (p->r) -- valid.
syllogism = Implies(And(Implies(p, q), Implies(q, r)), Implies(p, r))
assert is_valid(syllogism)

# Equivalence is validity of an IFF (MCS 3.3): the circuit simplification
# A OR (NOT(A) AND B)  ==  A OR B from MCS 3.2.
A, B = Bools("A B")
simplification = (Or(A, And(Not(A), B)) == Or(A, B))
assert is_valid(simplification)

# Affirming the consequent: (p->q) & q => p -- NOT valid. z3 hands us the bug.
fallacy = Implies(And(Implies(p, q), q), p)
assert not is_valid(fallacy)

# The MCS 3.5 SAT example -- a CNF formula. Satisfiable, but not valid.
mcs_35 = And(Or(p, q, r), Or(Not(p), Not(q)),
             Or(Not(p), Not(r)), Or(Not(r), Not(q)))
assert is_satisfiable(mcs_35)
assert not is_valid(mcs_35)

print("distributivity valid:", is_valid(distrib))
print("De Morgan valid:", is_valid(de_morgan))
print("hypothetical syllogism valid:", is_valid(syllogism))
print("circuit simplification valid:", is_valid(simplification))
print("affirming-the-consequent counterexample:",
      counterexample(fallacy))
print("MCS 3.5 formula satisfiable:", is_satisfiable(mcs_35))
