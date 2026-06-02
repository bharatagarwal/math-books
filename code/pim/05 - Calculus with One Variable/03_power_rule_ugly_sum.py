# uv run --with sympy python \
#   "code/pim/05 - Calculus with One Variable/03_power_rule_ugly_sum.py"
# Theorem 8.7 factors x^n - c^n = (x - c) * (the "ugly sum"),
#   ugly sum = x^{n-1} + x^{n-2}c + ... + x c^{n-2} + c^{n-1}.
# Plugging x = c into the ugly sum gives n*c^{n-1}, which is why
# the derivative of x^n is n*x^{n-1} (Theorem 8.8). We verify both
# the identity and the resulting power rule symbolically.
import sympy as sp

x, c = sp.symbols("x c")

for n in range(1, 9):
    ugly = sum(x ** (n - 1 - j) * c**j for j in range(n))
    # The factoring identity must hold as a polynomial identity.
    assert sp.expand((x - c) * ugly - (x**n - c**n)) == 0
    # The ugly sum at x = c collapses to n terms each c^{n-1}.
    assert sp.simplify(ugly.subs(x, c) - n * c ** (n - 1)) == 0
    # And that equals the actual derivative of x^n.
    assert sp.diff(x**n, x).subs(x, c) == n * c ** (n - 1)
    print(f"n={n}: (x-c)*ugly == x^{n}-c^{n}, "
          f"ugly(c) = {n}*c^{n - 1} = d/dx x^{n}")

print("\nThe ugly sum explains the power rule d/dx x^n = n x^(n-1).")
