# Z3 can reason about quantifiers directly
from z3 import *

n = Int('n')
# ∀n ≥ 0: n² + n + 41 is prime → FALSE (counterexample at n=40)
claim = ForAll(n, Implies(n >= 0, IsPrime(n*n + n + 41)))
# Z3 finds n=40 disproves it

# ∃n ≥ 0: n² + n + 41 is NOT prime → TRUE
negation = Exists(n, And(n >= 0, Not(IsPrime(n*n + n + 41))))
