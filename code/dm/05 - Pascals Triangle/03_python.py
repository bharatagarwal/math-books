# uv run --with hypothesis --with pytest pytest -q
"""Property-based tests (Hypothesis) for the Pascal-Triangle identities.

Where sympy proves the identities in closed form for a *symbolic* n, these
tests hammer them with many randomized concrete (n, k) values -- a different
kind of evidence, exercising integer arithmetic directly. We use math.comb so
the tests are independent of the recurrence code in 01_python.py.
"""
from math import comb

from hypothesis import given, settings
from hypothesis import strategies as st


@given(n=st.integers(min_value=0, max_value=400))
@settings(max_examples=200)
def test_recurrence(n):
    # C(n,k) = C(n-1,k-1) + C(n-1,k) -- the fundamental property (5).
    for k in range(1, n):
        assert comb(n, k) == comb(n - 1, k - 1) + comb(n - 1, k)


@given(n=st.integers(min_value=0, max_value=400))
@settings(max_examples=200)
def test_row_sum(n):
    # sum_{k} C(n,k) = 2^n  (exercise 5.3).
    assert sum(comb(n, k) for k in range(n + 1)) == 2 ** n


@given(n=st.integers(min_value=1, max_value=400))
@settings(max_examples=200)
def test_alternating_sum(n):
    # sum_{k} (-1)^k C(n,k) = 0  for n >= 1.
    assert sum((-1) ** k * comb(n, k) for k in range(n + 1)) == 0


@given(n=st.integers(min_value=0, max_value=300))
@settings(max_examples=200)
def test_sum_of_squares(n):
    # sum_{k} C(n,k)^2 = C(2n, n)  -- identity (6).
    assert sum(comb(n, k) ** 2 for k in range(n + 1)) == comb(2 * n, n)


@given(data=st.data())
@settings(max_examples=300)
def test_hockey_stick(data):
    # C(n,0)+C(n+1,1)+...+C(n+k,k) = C(n+k+1, k)  -- identity (7).
    n = data.draw(st.integers(min_value=0, max_value=300))
    k = data.draw(st.integers(min_value=0, max_value=300))
    assert sum(comb(n + i, i) for i in range(k + 1)) == comb(n + k + 1, k)


@given(data=st.data())
@settings(max_examples=300)
def test_partial_alternating_sum(data):
    # Stopping the alternating sum early: sum_{i=0}^{k} (-1)^i C(n,i)
    # = (-1)^k C(n-1, k)  -- the book's "stop earlier" result.
    n = data.draw(st.integers(min_value=1, max_value=300))
    k = data.draw(st.integers(min_value=0, max_value=n))
    partial = sum((-1) ** i * comb(n, i) for i in range(k + 1))
    assert partial == (-1) ** k * comb(n - 1, k)
