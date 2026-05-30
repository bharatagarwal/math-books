# uv run --with sympy python
"""Symbolic proofs (not just spot-checks) of the three closed forms the chapter
derives by induction. sympy.Sum closes each sum in terms of n, so equality holds
for ALL n at once -- exactly what induction buys you over a finite table.

  - Sum of the first n odd numbers      = n^2           (eq. (2))
  - Number of subsets of an n-set       = 2^n           (Theorem 2.1, re-proved)
  - Regions cut by n lines (gen. pos.)  = 1 + n(n+1)/2  (Theorem 3.1)
"""
import sympy as sp

n, k = sp.symbols("n k", integer=True, nonnegative=True)

# (2)  1 + 3 + ... + (2n-1) = n^2.  The k-th odd number is 2k-1.
odd_sum = sp.summation(2 * k - 1, (k, 1, n))
odd_sum = sp.simplify(odd_sum)
print(f"sum_(k=1..n) (2k-1) = {odd_sum}")
assert sp.simplify(odd_sum - n**2) == 0, "odd-sum identity failed"

# Reproduce the book's table (n = 1..10 gives 1,4,9,...,100).
table = [int(odd_sum.subs(n, m)) for m in range(1, 11)]
print(f"table n=1..10        = {table}")
squares = [m * m for m in range(1, 11)]
assert table == squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Theorem 3.1 region count, built the way the book builds it:
# start at 1 region (0 lines), then add 1+2+...+n.
regions = sp.simplify(1 + sp.summation(k, (k, 1, n)))
print(f"regions(n)           = {sp.factor(regions)}")
closed_form = 1 + n * (n + 1) / 2
assert sp.simplify(regions - closed_form) == 0, "region formula failed"

# The book also writes the count as 1 + n + C(n,2): check the two forms agree.
alt = 1 + n + sp.binomial(n, 2)
assert sp.simplify(regions - alt) == 0, "1+n(n+1)/2 != 1+n+C(n,2)"
print("regions  ==  1 + n + C(n,2)   (both closed forms agree symbolically)")

# Reproduce the book's region table: n=0,1,2,3,4 -> 1,2,4,7,11.
rtab = [int(regions.subs(n, m)) for m in range(0, 5)]
print(f"region table n=0..4  = {rtab}")
assert rtab == [1, 2, 4, 7, 11]

# Theorem 2.1 (subsets) re-proved the chapter's way: subsets of an n-set
# split into those NOT containing a (2^(n-1) of them) and those containing
# a (2^(n-1)).  So f(n) = 2*f(n-1), f(0)=1.  I.e. 2^(n-1) + 2^(n-1) = 2^n.
lhs = 2 ** (n - 1) + 2 ** (n - 1)
assert sp.simplify(lhs - 2**n) == 0, "subset split 2^(n-1)+2^(n-1) != 2^n"
print("subsets: 2^(n-1) + 2^(n-1)  ==  2^n   (containing/not split)")

print("ALL SYMBOLIC IDENTITIES PROVED")
