# uv run --with sympy python code/bradfield/01-counting/08_pascal_explore.py
# INTUITION: print Pascal's triangle and let the patterns JUMP OUT before we
# prove any of them. Each pattern below is something you can SEE in the numbers,
# then we connect it to a counting story.
import sympy as sp

N = 7
rows = [[int(sp.binomial(n, k)) for k in range(n + 1)] for n in range(N + 1)]

# Print it centered, the way it's usually drawn.
width = len(" ".join(map(str, rows[-1])))
print("Pascal's triangle:")
for r in rows:
    print(" ".join(map(str, r)).center(width))

# Pattern 1 -- it's left-right symmetric: C(n,k) = C(n,n-k).
#   "choosing which k to include = choosing which n-k to leave out."
print("\nsymmetry  C(n,k)=C(n,n-k):", all(r == r[::-1] for r in rows))

# Pattern 2 -- each entry is the SUM of the two above it (Pascal's rule).
#   "fix one element: your subset either contains it or it doesn't."
print("each = sum of two above  :",
      all(rows[n][k] == rows[n-1][k-1] + rows[n-1][k]
          for n in range(1, N + 1) for k in range(1, n)))

# Pattern 3 -- the rows sum to powers of two (the subset count again!).
print("row sums                 :", [sum(r) for r in rows], "= powers of 2")

# Pattern 4 -- the "hockey stick": a diagonal sums to the entry below-right.
#   sum_{i=k}^{n} C(i,k) = C(n+1,k+1).
hockey = sum(rows[i][2] for i in range(2, 6)) == int(sp.binomial(6, 3))
print("hockey-stick identity    :", hockey)
