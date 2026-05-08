# uv run --with sympy python
from sympy import isprime

def goldbach(n):
    """Find two primes that sum to n, or None if impossible."""
    for p in range(2, n // 2 + 1):
        if isprime(p) and isprime(n - p):
            return (p, n - p)
    return None

# Verify for even numbers up to 1000
for n in range(4, 1001, 2):
    result = goldbach(n)
    if result is None:
        print(f"Counterexample found: {n}")
        break
else:
    print("All even numbers 4-1000 satisfy Goldbach")
# Output: All even numbers 4-1000 satisfy Goldbach
