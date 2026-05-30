# uv run --with sympy python
"""Reproduce the chapter's table of ratios F_{n+1}/F_n -> the golden ratio.

Section 6.3 experiments with consecutive ratios 1/1, 2/1, 3/2, 5/3, ...
and observes they hover around 1.618. This script reproduces every printed
value to 9 decimals and shows the limit equals the golden ratio
q1 = (1+sqrt5)/2, the positive root of q^2 = q + 1. Exact rational
arithmetic (sympy) avoids any floating-point drift.
"""
import sympy as sp

# Fibonacci via the recurrence (exact integers).
F = [0, 1]
while len(F) < 20:
    F.append(F[-1] + F[-2])

# The book's printed table: pairs (F_{n+1}, F_n) and their decimal ratio.
book = {
    (1, 1): "1.000000000", (2, 1): "2.000000000", (3, 2): "1.500000000",
    (5, 3): "1.666666667", (8, 5): "1.600000000", (13, 8): "1.625000000",
    (21, 13): "1.615384615", (34, 21): "1.619047619", (55, 34): "1.617647059",
    (89, 55): "1.618181818", (144, 89): "1.617977528",
    (233, 144): "1.618055556", (377, 233): "1.618025751",
}

print(f"{'ratio':>10}  {'value (9 dp)':>12}  {'matches book?'}")
all_ok = True
for (num, den), printed in book.items():
    val = sp.Rational(num, den)
    # Round to 9 decimal places the same way the book displays.
    shown = f"{sp.Float(val, 30):.9f}"
    ok = (shown == printed)
    all_ok &= ok
    mark = "yes" if ok else "NO  expected " + printed
    print(f"{num:>4}/{den:<4}  {shown:>12}  {mark}")

assert all_ok, "a ratio disagreed with the book"

# Limit of F_{n+1}/F_n is the golden ratio (positive root of q^2 = q + 1).
phi = (1 + sp.sqrt(5)) / 2
print("\ngolden ratio (1+sqrt5)/2 =", phi.evalf(12))
print("F_19/F_18                =", sp.Rational(F[19], F[18]).evalf(12))
# Show convergence: |F_{n+1}/F_n - phi| -> 0
for n in (10, 15, 18):
    err = sp.Abs(sp.Rational(F[n + 1], F[n]) - phi)
    print(f"|F_{n+1}/F_{n} - phi| = {err.evalf(6)}")
print("OK: ratios reproduce the book and converge to the golden ratio")
