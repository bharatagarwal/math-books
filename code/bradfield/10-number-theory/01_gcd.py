# uv run python code/bradfield/10-number-theory/01_gcd.py
# Divisibility and the Euclidean algorithm -- the oldest nontrivial algorithm.
import math

def gcd(a, b):
    # Euclid: gcd(a,b) = gcd(b, a mod b). Each step shrinks the problem fast.
    while b:
        a, b = b, a % b
    return a

# Agrees with the standard library across a wide range (gcd(a,0)=a included).
assert all(gcd(a, b) == math.gcd(a, b)
           for a in range(1, 150) for b in range(0, 150))

def lcm(a, b):
    return a // gcd(a, b) * b

# The fundamental link between gcd and lcm: gcd(a,b) * lcm(a,b) = a*b.
assert gcd(48, 36) == 12 and lcm(48, 36) == 144
assert all(gcd(a, b) * lcm(a, b) == a * b
           for a in range(1, 80) for b in range(1, 80))

print("gcd(48,36) =", gcd(48, 36), " lcm(48,36) =", lcm(48, 36))
print("Euclid matches math.gcd; gcd*lcm = a*b verified")
