# uv run --with sympy python code/bradfield/06-induction/01_induction_sums.py
# Verification demo: every closed form LL proves by induction in ch 3,
# checked two ways -- brute summation == closed form for many n, AND
# sympy proves the symbolic identity for a free variable n.
import sympy as sp


def check_numerically():
    for n in range(0, 50):
        # sum of first n odd numbers = n^2
        assert sum(2 * k - 1 for k in range(1, n + 1)) == n ** 2
        # little Gauss: 1 + 2 + ... + n = n(n+1)/2
        assert sum(range(1, n + 1)) == n * (n + 1) // 2
        # sum of squares = n(n+1)(2n+1)/6
        assert (sum(k * k for k in range(1, n + 1))
                == n * (n + 1) * (2 * n + 1) // 6)
        # sum of powers of 2: 1 + 2 + ... + 2^n = 2^(n+1) - 1
        assert (sum(2 ** k for k in range(0, n + 1))
                == 2 ** (n + 1) - 1)
    print("numeric checks pass for n = 0..49")


def check_symbolically():
    n, k = sp.symbols("n k", integer=True, nonnegative=True)
    # sympy evaluates each Sum to a closed form; we confirm it matches LL.
    odds = sp.summation(2 * k - 1, (k, 1, n))
    gauss = sp.summation(k, (k, 1, n))
    squares = sp.summation(k ** 2, (k, 1, n))
    powers = sp.summation(2 ** k, (k, 0, n))
    assert sp.simplify(odds - n ** 2) == 0
    assert sp.simplify(gauss - n * (n + 1) / 2) == 0
    assert sp.simplify(squares - n * (n + 1) * (2 * n + 1) / 6) == 0
    assert sp.simplify(powers - (2 ** (n + 1) - 1)) == 0
    print("sympy closed forms:")
    print("  sum of odds   =", sp.factor(odds))
    print("  little Gauss  =", sp.factor(gauss))
    print("  sum of squares=", sp.factor(squares))
    print("  powers of two =", sp.simplify(powers))


if __name__ == "__main__":
    check_numerically()
    check_symbolically()
