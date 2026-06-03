# uv run --with sympy python
# Big sums and products — the Σ and Π notation in code.
from sympy import Sum, Product, Symbol, oo, Rational

n = Symbol('n', positive=True, integer=True)
k = Symbol('k', positive=True, integer=True)

# Σ_{n=0}^{∞} 1/2^n = 2  (geometric series)
geo = Sum(1 / 2**n, (n, 0, oo))
print(f"Σ 1/2^n (n=0..∞) = {geo.doit()}")

# Π_{j=0}^{5} (2j+1) = 1 × 3 × 5 × 7 × 9 × 11
j = Symbol('j')
prod = Product(2*j + 1, (j, 0, 5))
print(f"Π (2j+1) (j=0..5) = {prod.doit()}")

# Euler's product over primes (first 5 terms)
from sympy import isprime
partial = 1
for p in range(2, 30):
    if isprime(p):
        partial *= (1 - Rational(1, p))
print(f"Π (1-1/p) for primes < 30 ≈ {float(partial):.6f}")
# Σ 1/2^n (n=0..∞) = 2
# Π (2j+1) (j=0..5) = 10395
# Π (1-1/p) for primes < 30 ≈ 0.209012
