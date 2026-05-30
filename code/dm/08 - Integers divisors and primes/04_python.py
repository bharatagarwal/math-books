# uv run --with z3-solver python
# The Miller-Rabin idea on 561 (end of section 8.7) as a
# divisibility-constraint check.  The book factors a^561 - a using
# x^2 - 1 = (x-1)(x+1) down to:
#   a^561 - a = a (a^35 - 1)(a^35 + 1)(a^70 + 1)(a^140 + 1)(a^280 + 1)
# If 561 were prime it would have to divide one of these factors (a
# prime dividing a product divides a factor, ex 8.3).  The book says:
# "already for a = 2, none hold."  We let Z3 search for a witness: is
# there ANY of the six factors that 561 divides when a = 2?  Z3 returns
# unsat -> no factor works -> 561 is NOT prime.
from z3 import Int, Solver, Or, sat, unsat

a = 2

# the six factors from the book's expansion (eqn 18), as concrete
# integers mod 561
factors = {
    "a":          a,
    "a^35 - 1":   pow(a, 35) - 1,
    "a^35 + 1":   pow(a, 35) + 1,
    "a^70 + 1":   pow(a, 70) + 1,
    "a^140 + 1":  pow(a, 140) + 1,
    "a^280 + 1":  pow(a, 280) + 1,
}

# Sanity: the product of these factors really is a^561 - a
# (the book's identity).
prod = 1
for v in factors.values():
    prod *= v
assert prod == pow(a, 561) - a, "factorization identity failed"
print("identity check:"
      " a*(a^35-1)(a^35+1)(a^70+1)(a^140+1)(a^280+1) == a^561 - a"
      "  :  True")

# Fermat/Carmichael: 561 | a^561 - a (561 is a Carmichael number)
# -- the premise holds.
print("561 | 2^561 - 2 :", (pow(a, 561) - a) % 561 == 0)

# Z3 model: introduce an unknown quotient q_i per factor and ask
# whether 561 can divide ANY single factor
# (factor_i = 561 * q_i for some integer q_i).
s = Solver()
clauses = []
for name, val in factors.items():
    q = Int(f"q_<{name}>")
    # "561 divides val"  <=>  exists integer q with val == 561*q
    clauses.append(val == 561 * q)
s.add(Or(*clauses))

result = s.check()
print("Z3: does 561 divide at least one factor (a=2)?", result)
assert result == unsat, "expected unsat: no factor divisible by 561"
print("=> unsat: 561 divides NONE of the six factors,"
      " so 561 cannot be prime.")

# Show the actual remainders so the unsat is concrete and inspectable.
for name, val in factors.items():
    print(f"   {name:>10}  mod 561 = {val % 561}")
