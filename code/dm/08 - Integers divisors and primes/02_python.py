# uv run --with hypothesis --with pytest pytest -q
# The Euclidean Algorithm (section 8.6) and the extended version
# (Theorem 8.8).  A hand-written gcd + extended gcd, property-tested
# with Hypothesis against math.gcd.  Also reproduces the book's traces:
#   gcd(300,18) = gcd(12,18) = gcd(12,6) = 6
#   gcd(89,55) = ... = 1  (consecutive Fibonacci -> worst case,
#                          Thm 8.7 / ex 8.26)
from math import gcd as math_gcd
from hypothesis import given, strategies as st


def euclid_gcd(a, b):
    """Euclid's algorithm exactly as the book states it: replace the
    larger by the remainder until one number is 0; gcd(a,0)=a (the
    book's convention)."""
    while a != 0 and b != 0:
        if a > b:
            a, b = b, a          # keep a <= b
        b = b % a                # replace larger by remainder
    return a + b                 # one of them is 0, return the other


def trace(a, b):
    """Record the reduced argument pairs the book writes out, as
    unordered {x,y} sets, e.g. gcd(89,55)=gcd(34,55)=gcd(34,21)=...
    Returns (gcd, list_of_pairs) where each pair is the new
    {remainder, divisor} after one reduction."""
    steps = []
    while a != 0 and b != 0:
        if a > b:
            a, b = b, a          # a <= b
        b = b % a                # replace larger by remainder
        steps.append({a, b})     # the new argument pair for next call
    return a + b, steps


def ext_gcd(a, b):
    """Extended Euclid: return (d, m, n) with
    d = gcd(a,b) = a*m + b*n (Thm 8.8)."""
    old_r, r = a, b
    old_m, m = 1, 0
    old_n, n = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_m, m = m, old_m - q * m
        old_n, n = n, old_n - q * n
    return old_r, old_m, old_n


def test_book_traces():
    # gcd(300,18): book shows gcd(300,18)=gcd(12,18)=gcd(12,6)=6
    d, steps = trace(300, 18)
    assert d == 6
    assert steps[:2] == [{12, 18}, {6, 12}]   # the pairs the book shows
    # gcd(89,55) (consecutive Fibonacci): book shows the long chain
    d, steps = trace(89, 55)
    assert d == 1
    assert steps[:5] == [{34, 55}, {34, 21}, {13, 21}, {13, 8}, {5, 8}]
    # gcd(101,100)=gcd(1,100)=1  (consecutive integers: one step)
    assert euclid_gcd(101, 100) == 1


@given(st.integers(min_value=1, max_value=10**12),
       st.integers(min_value=1, max_value=10**12))
def test_euclid_matches_math_gcd(a, b):
    assert euclid_gcd(a, b) == math_gcd(a, b)


@given(st.integers(min_value=1, max_value=10**12),
       st.integers(min_value=1, max_value=10**12))
def test_bezout_identity(a, b):
    """Theorem 8.8: the returned d equals gcd, and d = a*m + b*n."""
    d, m, n = ext_gcd(a, b)
    assert d == math_gcd(a, b)
    assert a * m + b * n == d


@given(st.integers(min_value=2, max_value=10**9),
       st.integers(min_value=2, max_value=10**9))
def test_step_bound_thm_8_7(a, b):
    """Theorem 8.7: the number of reduction steps is at most
    log2(a)+log2(b).  (Stated for a,b>=2; the degenerate case a=1
    or b=1 finishes in one step.)"""
    from math import log2
    _, steps = trace(a, b)
    assert len(steps) <= log2(a) + log2(b) + 1e-9


if __name__ == "__main__":
    d, steps = trace(300, 18)
    print("gcd(300,18) =", d,
          " pairs:", [tuple(sorted(s)) for s in steps])
    print("gcd(89,55) =", euclid_gcd(89, 55))
    dd, m, n = ext_gcd(300, 18)
    print(f"ext_gcd(300,18): d={dd}, m={m}, n={n}"
          f"  ->  300*{m}+18*{n} = {300*m + 18*n}")
