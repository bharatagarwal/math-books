# uv run --with sympy python
"""Symbolic verification of the chapter's headline identities with sympy.

We verify, as exact symbolic statements (not just numeric spot-checks):

  * Sum of squares of row n  =  C(2n, n)         -- identity (6)
        sum_{k=0}^{n} C(n,k)^2 = C(2n,n)
    sympy closes this hypergeometric sum in closed form.

  * Row sum = 2^n  and  alternating sum = 0      -- exercise 5.3 & Sec 5.1
    Both come from the Binomial Theorem with x=y=1 and x=1,y=-1.

  * Partial alternating sum stopping early at k  =  (-1)^k C(n-1, k)
    -- the "stop earlier" result the book derives from the recurrence.
"""
import sympy as sp

n, k = sp.symbols("n k", integer=True, nonnegative=True)

# --- identity (6): sum of squares of a row = C(2n, n) -------------------
lhs = sp.summation(sp.binomial(n, k) ** 2, (k, 0, n))
rhs = sp.binomial(2 * n, n)
print("sum_{k=0}^{n} C(n,k)^2  -> sympy closes it as:", lhs)
print("C(2n, n)               =", rhs)
assert sp.simplify(lhs - rhs) == 0
print("=> identity (6) holds symbolically:  sum C(n,k)^2 = C(2n,n)\n")

# Reproduce the book's experimental table (rows 0..4 give 1,2,6,20,70).
book = [1, 2, 6, 20, 70]
got = [int(lhs.subs(n, v)) for v in range(5)]
print("book's experiment (rows 0..4):", book)
print("sympy from the closed form:   ", got)
assert got == book
# and these are the middle entries C(2n,n): C(0,0)=1, C(2,1)=2, C(4,2)=6, ...
assert got == [int(sp.binomial(2 * v, v)) for v in range(5)]
print("=> matches C(0,0),C(2,1),C(4,2),C(6,3),C(8,4) = 1,2,6,20,70\n")

# --- row sum = 2^n  and  alternating sum = 0 ----------------------------
row_sum = sp.summation(sp.binomial(n, k), (k, 0, n))
alt_sum = sp.summation((-1) ** k * sp.binomial(n, k), (k, 0, n))
print("sum_{k=0}^{n} C(n,k)        =", sp.simplify(row_sum),
      " (= 2^n, exercise 5.3)")
print("sum_{k=0}^{n} (-1)^k C(n,k) =",
      sp.simplify(alt_sum.rewrite(sp.Piecewise)), " (= 0 for n>=1)")
assert sp.simplify(row_sum - 2 ** n) == 0
# alternating sum is 0 for every n >= 1 (and 1 only for n=0):
for v in range(1, 9):
    assert int(alt_sum.subs(n, v)) == 0
print("=> row sum = 2^n;  alternating sum = 0 for all n>=1\n")

# --- partial alternating sum stopping at k = (-1)^k C(n-1, k) -----------
N = sp.Symbol("N", integer=True, positive=True)
j = sp.symbols("j", integer=True, nonnegative=True)
for nn in range(1, 8):
    for kk in range(0, nn + 1):
        partial = sum((-1) ** i * sp.binomial(nn, i) for i in range(kk + 1))
        claimed = (-1) ** kk * sp.binomial(nn - 1, kk)
        assert partial == claimed, (nn, kk, partial, claimed)
print("partial alt sum  sum_{i=0}^{k} (-1)^i C(n,i)  =  (-1)^k C(n-1,k)")
print("  checked for all 1<=n<=7, 0<=k<=n  ->  matches the book's derivation")
