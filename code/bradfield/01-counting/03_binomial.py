# uv run --with sympy python code/bradfield/01-counting/03_binomial.py
# Binomial coefficients: Pascal's rule, symmetry, and the binomial theorem.
import sympy as sp

n, k, x, y = sp.symbols("n k x y")

# Symmetry: C(n,k) = C(n, n-k).
assert all(sp.binomial(8, k) == sp.binomial(8, 8 - k) for k in range(9))

# Pascal's rule: C(n,k) = C(n-1,k-1) + C(n-1,k).
assert all(
    sp.binomial(9, k) == sp.binomial(8, k - 1) + sp.binomial(8, k)
    for k in range(1, 9)
)

# Binomial theorem: (x+y)^n = sum_k C(n,k) x^k y^(n-k).
N = 6
lhs = sp.expand((x + y) ** N)
rhs = sp.expand(sum(sp.binomial(N, j) * x**j * y ** (N - j) for j in range(N + 1)))
assert sp.simplify(lhs - rhs) == 0

# Setting x = y = 1 recovers the subset count 2^n; x=1,y=-1 gives 0 (n>0).
assert sum(sp.binomial(N, j) for j in range(N + 1)) == 2**N
assert sum((-1) ** j * sp.binomial(N, j) for j in range(N + 1)) == 0

print("(x+y)^6 =", lhs)
print("row 6 of Pascal:", [int(sp.binomial(6, j)) for j in range(7)])
