# From the repo root run (deps: sympy):
#   uv run --with sympy python \
#     "code/pim/05 - Calculus with One Variable/"*difference_quotient.py
# Definition 8.6: f'(c) is the LIMIT of the difference quotient
#   (f(x) - f(c)) / (x - c)  as x -> c.
# We watch the numeric quotient march toward the exact symbolic
# derivative as x' slides halfway closer to c, again and again
# (exactly the "move x' halfway closer" process of Figure 8.5).
import sympy as sp

x = sp.Symbol("x")
f_expr = x**2 - 6 * x + 1          # the chapter's worked example
c = 3

f = sp.lambdify(x, f_expr, "math")
exact = sp.diff(f_expr, x).subs(x, c)   # symbolic f'(3)
print(f"symbolic f'(x) = {sp.diff(f_expr, x)}")
print(f"exact f'({c})  = {exact}\n")

xprime = c + 1.0                   # start a full unit away
prev_err = None
for step in range(12):
    quotient = (f(xprime) - f(c)) / (xprime - c)
    err = abs(quotient - float(exact))
    print(f"x'={xprime:.10f}  quotient={quotient:+.10f}  err={err:.2e}")
    if prev_err is not None and prev_err > 0:
        # halving the gap halves the error: this difference
        # quotient is itself linear in (x' - c).
        assert err < prev_err            # monotone improvement
    prev_err = err
    xprime = c + (xprime - c) / 2        # halfway closer to c

assert err < 1e-3
print(f"\nDifference quotient -> {exact} = the exact derivative.")
