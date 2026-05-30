# uv run python code/bradfield/10-number-theory/02_bezout.py
# The EXTENDED Euclidean algorithm: gcd(a,b) = a*x + b*y (Bezout's identity).
# This is what makes modular inverses -- and therefore RSA -- computable.
import math

def ext_gcd(a, b):
    if b == 0:
        return (a, 1, 0)            # gcd(a,0)=a = a*1 + 0*0
    g, x, y = ext_gcd(b, a % b)
    return (g, y, x - (a // b) * y)  # back-substitute the Bezout coefficients

# For every pair, the returned (x, y) really do witness the gcd.
for a in range(1, 100):
    for b in range(1, 100):
        g, x, y = ext_gcd(a, b)
        assert g == math.gcd(a, b)
        assert a * x + b * y == g    # Bezout identity holds exactly

# Modular inverse: a^{-1} mod n EXISTS iff gcd(a,n)=1, and Bezout hands it over.
# From a*x + n*y = 1 we get a*x ≡ 1 (mod n), so x mod n is the inverse.
def modinv(a, n):
    g, x, _ = ext_gcd(a, n)
    assert g == 1, "inverse exists only when gcd(a,n)=1"
    return x % n

assert (3 * modinv(3, 7)) % 7 == 1
assert all((a * modinv(a, n)) % n == 1
           for n in range(2, 50) for a in range(1, n) if math.gcd(a, n) == 1)

print("Bezout: gcd(240,46) =", ext_gcd(240, 46))
print("3^{-1} mod 7 =", modinv(3, 7), "(since 3*5 = 15 ≡ 1 mod 7)")
