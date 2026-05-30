# uv run --with hypothesis --with pytest pytest -q
"""Property-test the Fibonacci identities from Section 6.2 with Hypothesis.

Instead of checking a handful of cases, Hypothesis throws hundreds of
random n at each identity. We verify, using exact integer Fibonacci
numbers:

  * sum identity      F_0+F_1+...+F_n = F_{n+2} - 1            (page 6.2)
  * Cassini  (6.5 d)  F_{n-1} F_{n+1} - F_n^2 = (-1)^n
  * sum of squares (6.5 c)  F_0^2+...+F_n^2 = F_n * F_{n+1}
  * odd-index sum (6.5 a)   F_1+F_3+...+F_{2n-1} = F_{2n}

The recurrence is the only thing we trust; the closed-form/identities are
the claims under test.
"""
from functools import lru_cache
from hypothesis import given, strategies as st


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """F_0=0, F_1=1, F_{n+1}=F_n+F_{n-1} (recurrence; valid for n>=0)."""
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def test_book_seed_values():
    # The chapter's explicit values F_1..F_5 = 1,1,2,3,5 and the listed prefix.
    assert [fib(k) for k in range(18)] == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    ]


@given(st.integers(min_value=0, max_value=400))
def test_sum_identity(n):
    # F_0 + F_1 + ... + F_n = F_{n+2} - 1
    assert sum(fib(k) for k in range(n + 1)) == fib(n + 2) - 1


@given(st.integers(min_value=1, max_value=400))
def test_cassini(n):
    # F_{n-1} F_{n+1} - F_n^2 = (-1)^n         (Exercise 6.5 d)
    assert fib(n - 1) * fib(n + 1) - fib(n) ** 2 == (-1) ** n


@given(st.integers(min_value=0, max_value=400))
def test_sum_of_squares(n):
    # F_0^2 + ... + F_n^2 = F_n * F_{n+1}      (Exercise 6.5 c)
    assert sum(fib(k) ** 2 for k in range(n + 1)) == fib(n) * fib(n + 1)


@given(st.integers(min_value=1, max_value=400))
def test_odd_index_sum(n):
    # F_1 + F_3 + ... + F_{2n-1} = F_{2n}      (Exercise 6.5 a)
    assert sum(fib(2 * k - 1) for k in range(1, n + 1)) == fib(2 * n)
