# uv run --with sympy python
"""Derive Binet's closed form (Theorem 6.1) from the recurrence.

The recurrence is F_{n+1} = F_n + F_{n-1}.

We do NOT hand the closed form to SymPy. We give it only the recurrence
and the two initial values F_0=0, F_1=1 (the chapter's definition) and let
rsolve solve it, exactly mirroring the book's "geometric progression c*q^n"
derivation: the characteristic equation q^2 = q + 1 produces the golden
ratio q1=(1+sqrt5)/2 and its conjugate q2=(1-sqrt5)/2, and the closed form
is (q1^n - q2^n)/sqrt5.
"""
import sympy as sp

n = sp.Symbol("n", integer=True)
F = sp.Function("F")

# The recurrence as homogeneous form: F(n) - F(n-1) - F(n-2) = 0,
# with the chapter's initial conditions F_0 = 0, F_1 = 1.
recurrence = F(n) - F(n - 1) - F(n - 2)
closed = sp.rsolve(recurrence, F(n), {F(0): 0, F(1): 1})
closed = sp.simplify(closed)
print("rsolve closed form  :", closed)

# Theorem 6.1 as printed in the book.
q1 = (1 + sp.sqrt(5)) / 2
q2 = (1 - sp.sqrt(5)) / 2
binet = (q1**n - q2**n) / sp.sqrt(5)
print("Theorem 6.1 (Binet) :", binet)

# Characteristic equation q^2 = q + 1 -> the golden ratio and conjugate.
q = sp.Symbol("q")
roots = sp.solve(sp.Eq(q**2, q + 1), q)
print("roots of q^2=q+1    :", sorted(roots, key=lambda r: float(r)))

# Prove the two expressions are identically equal as functions of n.
diff = sp.simplify(closed - binet)
print("rsolve - Binet      :", diff)
assert diff == 0, "rsolve solution does not match Theorem 6.1"

# And confirm both reproduce the book's listed sequence
#   0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597
expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
            55, 89, 144, 233, 377, 610, 987, 1597]
vals = [int(sp.nsimplify(binet.subs(n, k))) for k in range(len(expected))]
print("F_0..F_17 via Binet :", vals)
assert vals == expected, "closed form does not reproduce the book's sequence"
print("OK: derived Binet from recurrence; matches Theorem 6.1 and the list")
