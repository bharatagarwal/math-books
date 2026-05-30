# uv run python code/bradfield/10-number-theory/03_modular.py
# Modular arithmetic, fast exponentiation, and the two theorems crypto rests on.
import math

def power_mod(base, exp, mod):
    # Square-and-multiply: O(log exp) mults, never forming huge numbers.
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result

# Matches Python's built-in pow(b, e, m) everywhere.
assert all(power_mod(b, e, m) == pow(b, e, m)
           for b in range(1, 20) for e in range(0, 15) for m in range(2, 20))

def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))

# FERMAT'S LITTLE THEOREM: if p is prime and gcd(a,p)=1, then a^(p-1) ≡ 1 mod p.
primes = [p for p in range(2, 60) if is_prime(p)]
for p in primes:
    assert all(power_mod(a, p - 1, p) == 1 for a in range(1, p))

# EULER'S THEOREM generalizes it: a^phi(n) ≡ 1 mod n whenever gcd(a,n)=1, where
# phi(n) counts the integers in 1..n coprime to n. (This is the engine of RSA.)
def phi(n):
    return sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)

for n in range(2, 40):
    assert all(power_mod(a, phi(n), n) == 1
               for a in range(1, n) if math.gcd(a, n) == 1)

print("fast modular exponentiation matches pow()")
print("Fermat a^(p-1)=1 mod p and Euler a^phi(n)=1 mod n both verified")
print("phi(10) =", phi(10), " phi(12) =", phi(12))
