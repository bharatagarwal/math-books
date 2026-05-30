# uv run python code/bradfield/11-cryptography/01_rsa.py
"""RSA: key generation, encrypt/decrypt, and the trapdoor.

Follows LL ch 16, section 16.4. Uses LL's own tiny example:
p=5, q=11, n=55, phi=(p-1)(q-1)=40, e=3, d=27. Encryption is
c = m^e mod n, decryption m = c^d mod n. Euler's theorem (LL ch 8)
guarantees (m^e)^d = m mod n. We also show the trapdoor: the
factorization of n hands you phi, hence the private exponent d.
"""
from math import gcd


def egcd(a, b):
    """Extended Euclid: return (g, x, y) with a*x + b*y = g."""
    if b == 0:
        return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


def modinv(e, phi):
    """Modular inverse of e mod phi via extended Euclid."""
    g, x, _ = egcd(e, phi)
    assert g == 1, "e and phi must be coprime"
    return x % phi


def keygen(p, q, e):
    """Build an RSA key from primes p, q and exponent e (LL 16.4)."""
    n = p * q
    phi = (p - 1) * (q - 1)
    assert gcd(e, phi) == 1, "e must be coprime to phi(n)"
    d = modinv(e, phi)
    return n, phi, e, d


def main():
    # LL's worked example: p=5, q=11 (tiny, so NOT secure).
    p, q, e = 5, 11, 3
    n, phi, e, d = keygen(p, q, e)
    print(f"public key (n, e) = ({n}, {e})")
    print(f"private exponent d = {d}  (since e*d = {e*d}"
          f" = {e*d // phi}*{phi} + 1)")
    assert (e * d) % phi == 1

    # LL sends m = 7 and gets ciphertext c = 13.
    m = 7
    c = pow(m, e, n)
    rec = pow(c, d, n)
    print(f"m={m} -> c = {m}^{e} mod {n} = {c}"
          f" -> c^d mod n = {rec}")
    assert c == 13 and rec == m  # matches LL's hand computation

    # Decryption inverts encryption for every valid message.
    for m in range(n):
        assert pow(pow(m, e, n), d, n) == m
    print(f"verified: c^d recovers m for all {n} messages 0..{n-1}")

    # The trapdoor is the factorization of n. Knowing p, q gives
    # phi = (p-1)(q-1), hence d. Without it, an eavesdropper who
    # sees only (n, e) and c cannot derive d.
    phi_from_factors = (p - 1) * (q - 1)
    d_from_factors = modinv(e, phi_from_factors)
    print(f"trapdoor: factor n={n} as {p}*{q}"
          f" -> phi={phi_from_factors} -> d={d_from_factors}")
    assert d_from_factors == d


if __name__ == "__main__":
    main()
