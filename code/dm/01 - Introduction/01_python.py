# uv run --with sympy python
#
# Orientation demo: the verify-by-code methodology of this reader.
#
# The book opens by describing number theory as "the study of positive
# integers 1, 2, 3, ...". The very first thing one proves about those integers
# is the closed form for their running sum:
#
#       1 + 2 + ... + n  =  n(n+1)/2.
#
# Rather than trust the formula, we let a computer algebra system PROVE it
# symbolically. sympy.Sum evaluates the sum over a symbolic upper bound n
# (no specific number plugged in), and we check that the result is identically
# equal to the claimed closed form for ALL n. This is the whole spirit of the
# reader: state a mathematical fact, then back it with real, runnable tooling.

import sympy as sp

k, n = sp.symbols("k n", positive=True, integer=True)

# Symbolic sum 1 + 2 + ... + n, evaluated as a function of n (not a number).
closed_form = sp.Sum(k, (k, 1, n)).doit()
print("sympy evaluates  1 + 2 + ... + n  =", closed_form)

# The textbook's claimed closed form.
claimed = n * (n + 1) / 2

# Prove they are the SAME expression for every n by simplifying the difference.
difference = sp.simplify(closed_form - claimed)
print("closed_form - n(n+1)/2 simplifies to:", difference)
assert difference == 0, "symbolic identity failed"

# Sanity spot-check against a concrete value the way the book would by hand:
# 1 + 2 + ... + 100 = 100 * 101 / 2 = 5050 (the classic Gauss sum).
gauss = int(closed_form.subs(n, 100))
print("spot check n=100:  1 + 2 + ... + 100 =", gauss)
assert gauss == 5050

print("VERIFIED: 1 + 2 + ... + n = n(n+1)/2 holds symbolically for all n.")
