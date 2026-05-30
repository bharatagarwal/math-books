# uv run --with sympy python code/bradfield/05-proofs/07_sign_table.py
import sympy as sp

# INTUITION DEMO: before proving "a^3 > a => a^5 > a", DISCOVER the
# shape of the truth set by building a sign table by hand. a^3 - a
# factors as a(a-1)(a+1); the sign flips at the roots -1, 0, 1.

a = sp.Symbol("a", real=True)
expr3 = sp.factor(a**3 - a)   # a*(a - 1)*(a + 1)
print("a^3 - a factors as:", expr3)

# Sample one point inside each interval cut out by the roots -1,0,1.
samples = [sp.Rational(-2), sp.Rational(-1, 2),
           sp.Rational(1, 2), sp.Rational(2)]
print("\n   a      a^3 - a    a^5 - a   sign agree?")
for v in samples:
    s3 = a**3 - a
    s5 = a**5 - a
    d3 = s3.subs(a, v)
    d5 = s5.subs(a, v)
    agree = (d3 > 0) == (d5 > 0)
    print(f"{str(v):>6}   {str(d3):>7}    {str(d5):>7}    {agree}")

# Wherever a^3 - a > 0, we also see a^5 - a > 0: the implication's
# truth set (-1,0) U (1, inf) is contained in that of a^5 > a.
for v in samples:
    if (a**3 - a).subs(a, v) > 0:
        assert (a**5 - a).subs(a, v) > 0
print("\nwhere a^3 > a, the samples also have a^5 > a")
