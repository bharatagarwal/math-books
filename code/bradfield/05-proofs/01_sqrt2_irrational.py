# uv run --with sympy python code/bradfield/05-proofs/01_sqrt2_irrational.py
# Proof by contradiction: sqrt(2) is irrational. We verify the key steps.
import sympy as sp

# sympy's verdict (it knows the theorem):
assert sp.sqrt(2).is_rational is False
assert sp.sqrt(2).is_irrational is True

# The proof's engine is a parity argument. Suppose sqrt(2) = a/b in
# LOWEST terms, so a^2 = 2 b^2. Then a^2 is even, hence a is even (the
# contrapositive: an odd number squared is odd). Confirm it mod 2:
assert all((a % 2 == 1) == ((a * a) % 2 == 1) for a in range(1000))

# Write a = 2k. Then (2k)^2 = 2 b^2  =>  2 k^2 = b^2, so b^2 is even and b is
# even too. But then a and b share the factor 2 -- contradicting "lowest terms".
# Equivalently: a^2 = 2 b^2 has NO positive-integer solution. Search:
solutions = [(a, b) for b in range(1, 400)
             for a in [sp.Integer(2 * b * b)]  # need a^2 = 2 b^2
             if sp.sqrt(2 * b * b).is_integer]
assert solutions == []

print("sqrt(2) is irrational:", sp.sqrt(2).is_irrational)
print("a^2 = 2 b^2 has no positive integer solution")
