# uv run --with sympy python
# Binomial Theorem (Theorem 4.3): the coefficient of x^k y^(n-k)
# in (x+y)^n is C(n,k). We verify by symbolically expanding (x+y)^n
# and matching each coefficient to binomial(n,k). This reproduces
# the book's explicit expansions of (x+y)^2, (x+y)^3, (x+y)^4 and
# the (x+y)^5 line with coefficients C(5,0)..C(5,5) = 1,5,10,10,5,1.

import sympy as sp

x, y = sp.symbols("x y")


def check(n):
    expanded = sp.expand((x + y) ** n)
    coeffs = []
    for k in range(n + 1):
        # coefficient of x^k * y^(n-k)
        c = expanded.coeff(x, k).coeff(y, n - k)
        assert c == sp.binomial(n, k), (
            f"mismatch n={n} k={k}: {c} != C({n},{k})"
        )
        coeffs.append(int(c))
    return expanded, coeffs


# Reproduce the small cases printed in the book.
for n in (2, 3, 4, 5):
    expanded, coeffs = check(n)
    print(f"(x+y)^{n} = {expanded}")
    print(f"   coefficients = {coeffs}  (= C({n},0)..C({n},{n}))")

# Book's setting x=y=1 gives the row sum 2^n  (identity (4)).
row_sums = []
for n in range(0, 6):
    row = [int(sp.binomial(n, k)) for k in range(n + 1)]
    assert sum(row) == 2 ** n
    row_sums.append(sum(row))
print("Row sums match 2^n:", row_sums)

print("Binomial Theorem verified for n = 2..5.")
