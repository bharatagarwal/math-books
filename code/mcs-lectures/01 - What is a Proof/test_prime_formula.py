from hypothesis import given, strategies


@given(strategies.integers(min_value=0))
def test_prime_formula(n):
    val = n * n + n + 41

    for d in range(2, int(val**0.5) + 1):
        assert val % d != 0, f"n={n}: {val} is divisible by {d}"


if __name__ == "__main__":
    test_prime_formula()
