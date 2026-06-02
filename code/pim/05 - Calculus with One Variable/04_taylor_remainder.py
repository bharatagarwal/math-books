# uv run --with sympy python \
#   "code/pim/05 - Calculus with One Variable/04_taylor_remainder.py"
# The Adolescent Taylor Theorem (8.13) builds the degree-k polynomial
#   p_k(x) = sum_{n=0}^k f^{(n)}(a)/n! * (x-a)^n.
# For f = e^x at a = 0 this is 1 + x + x^2/2 + x^3/6 + ...
# The Taylor Theorem (8.14) says the leftover error is one more term
# with a "magical z"; here we just watch the empirical remainder
# shrink as the degree grows, and confirm the chapter's degree-4
# polynomial for e^x.
import sympy as sp

x = sp.Symbol("x")


def taylor(expr, a, k):
    terms = [expr.diff(x, n).subs(x, a) / sp.factorial(n) * (x - a) ** n
             for n in range(k + 1)]
    return sum(terms)


# Confirm the chapter's printed degree-4 Taylor poly of e^x at 0.
p4 = sp.expand(taylor(sp.exp(x), 0, 4))
assert p4 == 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24
print(f"degree-4 Taylor of e^x at 0: {p4}\n")

# Remainder |e^x - p_k(x)| at x = 1 must shrink toward zero with k.
target = sp.exp(1)
prev = None
for k in range(1, 9):
    pk = taylor(sp.exp(x), 0, k)
    err = abs(float(pk.subs(x, 1) - target))
    print(f"k={k}: p_k(1)={float(pk.subs(x, 1)):.8f}  "
          f"remainder={err:.2e}")
    if prev is not None:
        assert err < prev          # each extra term helps
    prev = err

assert prev < 1e-3
# sin x at 0 is the textbook alternating series x - x^3/6 + x^5/120.
p5_sin = sp.expand(taylor(sp.sin(x), 0, 5))
assert p5_sin == x - x**3 / 6 + x**5 / 120
print(f"\ndegree-5 Taylor of sin x at 0: {p5_sin}")
