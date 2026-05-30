# uv run --with hypothesis --with pytest pytest -q
# Pascal's recurrence (exercise 4.8): C(n,k) = C(n-1,k-1) + C(n-1,k).
# The book's concrete instance is C(90,5) = C(89,5) + C(89,4);
# 4.8(b) asks for the general identity. We pin the concrete case,
# then let Hypothesis hammer the general law over random (n,k),
# plus the two other chapter identities:
#   exercise 4.7:  C(n,2) + C(n+1,2) = n^2
#   identity (4):  sum_{k=0}^{n} C(n,k) = 2^n   (Binomial Theorem at x=y=1)

from math import comb

from hypothesis import given, settings
from hypothesis import strategies as st


def test_book_concrete_4_8a():
    # exercise 4.8(a), the exact numbers in the book
    assert comb(90, 5) == comb(89, 5) + comb(89, 4)
    assert comb(90, 5) == 43949268


@settings(max_examples=500)
@given(
    n=st.integers(min_value=1, max_value=400),
    k=st.integers(min_value=0, max_value=400),
)
def test_pascal_recurrence_general(n, k):
    # exercise 4.8(b): the general Pascal recurrence for 1 <= k <= n-1.
    # Outside that band the boundary cases still hold with C=0 conventions,
    # but we test the interesting interior band.
    if 1 <= k <= n - 1:
        assert comb(n, k) == comb(n - 1, k - 1) + comb(n - 1, k)


@settings(max_examples=300)
@given(n=st.integers(min_value=0, max_value=500))
def test_exercise_4_7(n):
    # C(n,2) + C(n+1,2) = n^2
    assert comb(n, 2) + comb(n + 1, 2) == n * n


@settings(max_examples=200)
@given(n=st.integers(min_value=0, max_value=200))
def test_row_sum_is_power_of_two(n):
    # identity (4): sum of a Pascal row is 2^n
    assert sum(comb(n, k) for k in range(n + 1)) == 2 ** n
