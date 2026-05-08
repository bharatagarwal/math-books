# Property-based test: for any even n, n² is even
from hypothesis import given, strategies as st

def is_even(n): return n % 2 == 0

@given(st.integers(min_value=0, max_value=1000)
       .filter(lambda n: n % 2 == 0))
def test_even_square_is_even(n):
    assert is_even(n * n)
