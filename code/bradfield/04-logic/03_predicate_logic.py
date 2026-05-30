# uv run --with z3-solver python code/bradfield/04-logic/03_predicate_logic.py
"""Predicate logic and quantifiers via Z3 (MCS 3.6).

MCS 3.6 stresses two traps: quantifier ORDER matters, and NEGATION
flips quantifiers. We check both -- first over the integers (where
"there is a greatest integer" is simply false), then over a tiny finite
domain modelling MCS's "Every American has a dream", where swapping the
quantifiers genuinely changes which models exist.
"""
from z3 import (Function, IntSort, BoolSort, ForAll, Exists, Int,
                Solver, Not, And, Or, Bool, sat, unsat)


def main() -> None:
    x, y = Int("x"), Int("y")

    # forall x exists y. x < y  -- valid over the integers (always a
    # bigger one). Negation unsat => the statement is valid.
    s = Solver()
    s.add(Not(ForAll([x], Exists([y], x < y))))
    print("forall x exists y (x<y) valid:", s.check() == unsat)

    # exists y forall x. x <= y  -- swapping the quantifiers asks for a
    # greatest integer, which does not exist. Unsatisfiable.
    s = Solver()
    s.add(Exists([y], ForAll([x], x <= y)))
    print("exists y forall x (x<=y) sat:", s.check() == sat)

    # Negation flips quantifiers (MCS 3.6.5):
    #   NOT(forall x. P(x))  iff  exists x. NOT P(x)
    P = Function("P", IntSort(), BoolSort())
    left = Not(ForAll([x], P(x)))
    right = Exists([x], Not(P(x)))
    s = Solver()
    s.add(Not(left == right))
    print("negation flips quantifier valid:", s.check() == unsat)

    quantifier_order_demo()


def quantifier_order_demo() -> None:
    """MCS 3.6.3 'Every American has a dream' over a 2x2 finite domain.

    H[a][d] = "American a has dream d". The two readings are:
      same shared dream:  exists d. forall a. H(a, d)
      personal dreams:    forall a. exists d. H(a, d)
    We hand Z3 a world where everyone dreams, but no single dream is
    shared, and ask which reading it satisfies.
    """
    # H is a 2x2 grid of Booleans: 2 Americans, 2 dreams.
    H = [[Bool(f"H_{a}_{d}") for d in range(2)] for a in range(2)]

    # World: American 0 dreams only dream 0; American 1 only dream 1.
    world = And(H[0][0], Not(H[0][1]), Not(H[1][0]), H[1][1])

    # personal: forall a. exists d. H(a, d)
    personal = And(*[Or(H[a][0], H[a][1]) for a in range(2)])
    # shared: exists d. forall a. H(a, d)
    shared = Or(And(H[0][0], H[1][0]), And(H[0][1], H[1][1]))

    s = Solver()
    s.add(world)
    s.add(personal)
    s.add(Not(shared))
    res = s.check()
    print("world with personal-but-not-shared dreams sat:", res == sat)
    # forall-exists is strictly weaker than exists-forall (MCS 3.6):
    # such a world exists, so the orders are NOT equivalent.
    assert res == sat


main()
