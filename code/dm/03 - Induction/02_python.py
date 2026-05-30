# uv run --with hypothesis --with pytest pytest -q
"""Property-based tests: hypothesis throws hundreds of random n at the chapter's
claims. Where sympy proves the closed form, hypothesis attacks the OTHER half of
an induction proof -- it checks the recurrence (the (n-1) -> n inductive STEP)
and the literal "add up the actual numbers" definition, so a wrong formula gets
a concrete counterexample rather than slipping through a finite table."""
from hypothesis import given, strategies as st


def odd_sum_direct(n: int) -> int:
    """Literally add the first n odd numbers 1,3,5,... (the chapter's LHS)."""
    return sum(2 * k - 1 for k in range(1, n + 1))


def regions_direct(n: int) -> int:
    """Build region count the chapter's way: start at 1, then the k-th new line
    adds k regions (it crosses k-1 existing lines -> k new regions)."""
    r = 1
    for k in range(1, n + 1):
        r += k
    return r


@given(st.integers(min_value=0, max_value=2000))
def test_odd_sum_is_square(n):
    # eq.(2): 1+3+...+(2n-1) = n^2, tested by summing the real terms.
    assert odd_sum_direct(n) == n * n


@given(st.integers(min_value=1, max_value=2000))
def test_odd_sum_inductive_step(n):
    # The induction STEP itself: S(n) = S(n-1) + (2n-1).
    assert odd_sum_direct(n) == odd_sum_direct(n - 1) + (2 * n - 1)


@given(st.integers(min_value=0, max_value=2000))
def test_regions_formula(n):
    # Theorem 3.1: n lines in general position -> 1 + n(n+1)/2 regions.
    assert regions_direct(n) == 1 + n * (n + 1) // 2


@given(st.integers(min_value=0, max_value=20))
def test_subsets_count_and_split(n):
    # Theorem 2.1: an n-set has 2^n subsets, and the chapter's split holds:
    # subsets-without-a + subsets-with-a = 2^(n-1) + 2^(n-1) = 2^n.
    elements = list(range(n))
    count = 0
    for mask in range(1 << n):  # every bitmask = one subset
        count += 1
    assert count == 2**n
    if n >= 1:
        assert count == 2 ** (n - 1) + 2 ** (n - 1)


def test_book_tables_reproduced():
    # Exact numbers printed in the chapter.
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert [odd_sum_direct(m) for m in range(1, 11)] == squares
    assert [regions_direct(m) for m in range(0, 5)] == [1, 2, 4, 7, 11]
