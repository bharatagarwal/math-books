# uv run python code/bradfield/05-proofs/04_well_ordering.py
# The Well Ordering Principle: every nonempty set of naturals has a
# LEAST element. WOP powers "smallest counterexample" proofs. Example:
# every integer n > 1 has a prime divisor. Proof: let C = the
# counterexamples; if nonempty, WOP gives a least one, m. m isn't prime
# (else m | m), so m = a*b with 1 < a < m. a < m, so a is NOT a
# counterexample: a has a prime divisor p. But p | a and a | m, so
# p | m -- m has a prime divisor after all. Contradiction. So C is empty.

def least_prime_divisor(n):
    # The constructive content of the proof: the least divisor > 1 is prime.
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return n  # n is prime

# Verify the theorem holds for every n in a wide range, and that the witness the
# WOP argument produces (the least divisor > 1) really is prime and divides n.
for n in range(2, 5000):
    p = least_prime_divisor(n)
    assert n % p == 0
    assert least_prime_divisor(p) == p  # p prime: least divisor is itself

# WOP itself, as code: scanning upward from 0 finds the least element of any
# nonempty subset of the naturals -- the principle is "the search terminates".
def wop_least(subset):
    n = 0
    while n not in subset:
        n += 1
    return n

assert wop_least({42, 7, 100, 7}) == 7
print("every n>1 has a prime divisor: verified 2..4999 via WOP witness")
print("least of {7,42,100} by upward search:", wop_least({42, 7, 100}))
