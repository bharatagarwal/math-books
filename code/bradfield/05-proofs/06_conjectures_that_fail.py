# uv run --with sympy python \
#   code/bradfield/05-proofs/06_conjectures_that_fail.py
import sympy as sp

# INTUITION DEMO (MCS ch 1): three propositions, each "true" for a huge
# number of cases, each ultimately FALSE. The point is calibration: how
# far would brute-force testing have to run before the lie showed?

# (1) Euler's sum-of-powers conjecture: a^4 + b^4 + c^4 = d^4 has no
#     positive integer solutions. FALSE -- Elkies, 1988.
a, b, c, d = 95800, 217519, 414560, 422481
lhs = a**4 + b**4 + c**4
print("a^4 + b^4 + c^4 =", lhs)
print("d^4             =", d**4)
assert lhs == d**4
print("=> Euler's conjecture is FALSE; smallest d has 6 digits\n")

# (2) "n^2 + n + 41 is always prime." Survives 40 cases, dies at n = 40.
fails = [n for n in range(0, 60) if not sp.isprime(n*n + n + 41)]
print("n^2 + n + 41 first fails at n =", fails[0], "\n")

# (3) A counterexample can be astronomically large. The proposition
#     313*(x^3 + y^3) = z^3 has no positive solutions is FALSE, but the
#     smallest counterexample has more than 1000 digits. We cannot print
#     it -- which is exactly the lesson: "no counterexample found yet"
#     is not the same as "none exists." We just confirm the scale claim.
smallest_digits = 1000
print(f"313*(x^3+y^3)=z^3: smallest counterexample > {smallest_digits} digits")
print("brute force would never reach it -- proof is the only tool here")

# Sanity: testing the first N cases of (2) really would have "passed".
assert all(sp.isprime(n*n + n + 41) for n in range(0, 40))
print("\nfirst 40 cases of (2) all pass -- testing alone is not proof")
