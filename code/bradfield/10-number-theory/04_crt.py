# uv run python code/bradfield/10-number-theory/04_crt.py
# The Chinese Remainder Theorem: a system of congruences with coprime moduli has
# a unique solution modulo the product. Used to speed up RSA and to split big
# computations into independent residues.
import math

def ext_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = ext_gcd(b, a % b)
    return (g, y, x - (a // b) * y)

def modinv(a, n):
    g, x, _ = ext_gcd(a, n)
    assert g == 1
    return x % n

def crt(remainders, moduli):
    # Assumes the moduli are pairwise coprime.
    M = math.prod(moduli)
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        x += r * Mi * modinv(Mi, m)
    return x % M

# Classic: x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7). Answer: 23.
rem, mod = [2, 3, 2], [3, 5, 7]
x = crt(rem, mod)
assert x == 23
assert all(x % m == r for r, m in zip(rem, mod))

# Brute force confirms uniqueness mod 3*5*7 = 105.
brute = [k for k in range(math.prod(mod))
         if all(k % m == r for r, m in zip(rem, mod))]
assert brute == [23]

print("CRT solution:", x, "(unique mod", math.prod(mod), ")")
