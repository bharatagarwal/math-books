# uv run python code/bradfield/06-induction/04_strong_induction.py
# Verification demo for the two MCS ch 5 strong-induction theorems.
# Strong induction reaches back to ALL smaller cases, not just n-1.


def can_make(amount, stamps=(3, 5), memo=None):
    """Can `amount` cents be made from the given stamp values?"""
    if memo is None:
        memo = {}
    if amount == 0:
        return True
    if amount < 0:
        return False
    if amount in memo:
        return memo[amount]
    result = any(can_make(amount - s, stamps, memo) for s in stamps)
    memo[amount] = result
    return result


def test_postage():
    # MCS 5.2.2: every postage >= 8 is makeable with 3- and 5-cent stamps.
    for n in range(8, 200):
        assert can_make(n), f"{n} not makeable"
    # 1, 2, 4, 7 are exactly the gaps below 8.
    assert [n for n in range(0, 8) if not can_make(n)] == [1, 2, 4, 7]
    print("all postage >= 8 makeable; gaps below 8 are 1,2,4,7")


def prime_factorization(n):
    """Return primes whose product is n (n > 1), found by strong
    induction: split off the smallest factor and recurse on a SMALLER
    number, which the hypothesis already handles."""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    return factors


def test_products_of_primes():
    # MCS 5.2.1: every integer > 1 is a product of primes.
    for n in range(2, 500):
        fs = prime_factorization(n)
        prod = 1
        for f in fs:
            prod *= f
        assert prod == n
        assert all(is_prime(f) for f in fs)
    print("every n in 2..499 is a product of primes")


def is_prime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))


if __name__ == "__main__":
    test_postage()
    test_products_of_primes()
