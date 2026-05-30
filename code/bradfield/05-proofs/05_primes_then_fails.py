# uv run --with sympy python code/bradfield/05-proofs/05_primes_then_fails.py
import sympy as sp

# INTUITION DEMO (MCS ch 1): Euler's polynomial f(n) = n^2 + n + 41.
# A test suite that checked n = 0..39 would report "all prime" and pass.
# We DISCOVER the first failure by just looking at the sequence grow.

def f(n):
    return n * n + n + 41

# Walk n upward; stop the "winning streak" at the first composite value.
initial_run = 0
counting = True
first_fail = None
for n in range(0, 45):
    val = f(n)
    prime = sp.isprime(val)
    if counting and prime:
        initial_run += 1
    elif counting and not prime:
        counting = False
        first_fail = n
    # Show the run so the "looks true forever" feeling is visible.
    if n < 5 or 38 <= n <= 41:
        tag = "prime" if prime else "NOT prime"
        print(f"f({n:2d}) = {val:5d}   {tag}")

print(f"\nf(n) was prime for n = 0..{initial_run - 1} (an unbroken run "
      f"of {initial_run})")
print(f"first n where f(n) is composite: {first_fail}")

# The proof of WHY it must fail: f(40) = 40*41 + 41 = 41 * 41.
assert f(40) == 41 * 41
assert not sp.isprime(f(40))
print("f(40) = 41 * 41  -- the structure no finite test would reveal")
