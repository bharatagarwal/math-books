# uv run --with sympy python
# Toy RSA (section 16.4) -- the full protocol with a complete
# encrypt -> decrypt round trip, plus the signature trick from the chapter.
# Keys are small enough to print but use the SAME steps the book describes:
#   m = p*q ;  pick e coprime to (p-1)(q-1) ;  d = e^{-1} mod (p-1)(q-1)
#   encrypt r = x^e mod m ;  decrypt x = r^d mod m   (via fast modular pow)
from sympy import nextprime, gcd, mod_inverse


def keygen(seed):
    p = nextprime(seed)
    q = nextprime(p + 10_000)        # two DISTINCT primes
    m = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:          # e relatively prime to (p-1)(q-1)
        e += 2
    d = mod_inverse(e, phi)          # Euclidean algorithm gives the private key
    assert (e * d) % phi == 1
    return (m, e), d, (p, q)


# Alice's keys.  m and e are public; d (and p, q) are secret.
(m, e), d, (p, q) = keygen(10**6)
print(f"Alice public key (m, e) = ({m}, {e}); private d = {d}")
print("check  e*d mod (p-1)(q-1) =", (e * d) % ((p - 1) * (q - 1)))

# Bob sends Alice the chess move Kf3 -> 1163 as the integer x (< m).
x = 1163
r = pow(x, e, m)                     # encrypt: x^e mod m, computed fast
back = pow(r, d, m)                  # decrypt: r^d mod m
print(f"x = {x} -> ciphertext r = {r} -> decrypt = {back}  ok? {back == x}")

# The chapter notes x^e is astronomically large but x^e mod m is tiny --
# fast modular exponentiation (repeated squaring) keeps it manageable.
print("x**e would have", len(str(x**e)), "digits; r mod m has", len(str(r)))

# Signature trick (section "Signatures, etc."): Bob signs with his OWN private
# key; anyone can check it with his public key, proving the message is his.
(mb, eb), db, _ = keygen(2 * 10**6)
msg = 4242 % mb
signature = pow(msg, db, mb)         # sign with Bob's PRIVATE key
verified = pow(signature, eb, mb)    # verify with Bob's PUBLIC key
print(f"signature verifies to original msg: {verified == msg}")
