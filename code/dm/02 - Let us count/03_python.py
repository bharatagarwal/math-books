# uv run --with hypothesis --with pytest pytest -q
# Property-based check of Theorem 2.4 ("the number of permutations of n
# objects is n!") and of the divide-out-the-overcount reasoning behind
# combinations. Hypothesis throws many random n (and k) at the claims;
# for small n we *actually enumerate* with itertools and compare to the
# closed form, so the property is grounded in real counting, not just algebra.

from itertools import permutations, combinations
from math import factorial, comb
from hypothesis import given, strategies as st


@given(n=st.integers(min_value=0, max_value=8))
def test_permutation_count_equals_factorial(n):
    """Theorem 2.4: #orderings of n distinct objects == n!.
    Enumerate every permutation of range(n) and count them."""
    enumerated = sum(1 for _ in permutations(range(n)))
    assert enumerated == factorial(n)


@given(data=st.data())
def test_combination_count_equals_binomial(data):
    """C(n,k) == number of k-subsets == n! / (k!(n-k)!).
    The party's 'count ordered tuples, then divide by k!' argument."""
    n = data.draw(st.integers(min_value=0, max_value=8))
    k = data.draw(st.integers(min_value=0, max_value=n))
    enumerated = sum(1 for _ in combinations(range(n), k))
    assert enumerated == comb(n, k)
    # ordered selections (n*(n-1)*...) divided by k! recovers the same count
    falling = factorial(n) // factorial(n - k)
    assert enumerated * factorial(k) == falling


@given(n=st.integers(min_value=2, max_value=9))
def test_handshake_pairs_are_binomial_n_2(n):
    """Handshakes among n people = C(n,2) = n(n-1)/2 (Eve's '42/2 = 21')."""
    enumerated = sum(1 for _ in combinations(range(n), 2))
    assert enumerated == comb(n, 2) == n * (n - 1) // 2
