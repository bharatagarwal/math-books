# uv run --with sympy python
from sympy import nextprime, factorint
import time

p = nextprime(10**20)
q = nextprime(10**20 + 10**17)
t0 = time.time()
N = p * q
t_mult = time.time() - t0
print(f"p = {p}")
print(f"q = {q}")
print(f"N = {N} ({len(str(N))} digits)")
print(f"Multiply: {t_mult:.6f}s")

t0 = time.time()
factors = factorint(N)
t_fact = time.time() - t0
print(f"Factor:   {t_fact:.3f}s")
print(f"Recovered: {factors}")
# Output:
# Multiply: 0.000000s
# Factor:   ~0.3s
# At 25 digits, factoring already exceeds 30s. RSA uses 300+ digit primes.
