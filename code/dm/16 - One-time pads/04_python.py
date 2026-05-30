# uv run --with sympy --with hypothesis --with pytest pytest -q
# RSA correctness IS Fermat's little theorem (the "black math magic" of 16.4).
# The book proves: since (p-1)(q-1) divides ed-1, the map x -> x^{ed} mod m is
# the identity, because Fermat's theorem makes x^p == x (mod p) for every x.
# We turn that proof into VERIFIED, property-based tests with Hypothesis.
from sympy import nextprime, gcd, mod_inverse
from hypothesis import given, settings, strategies as st


def make_rsa(seed):
    p = nextprime(seed)
    q = nextprime(p + 50)
    m, phi = p * q, (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    d = mod_inverse(e, phi)
    return p, q, m, e, d


P, Q, M, E, D = make_rsa(5000)


# --- Fermat's "Little" Theorem (Theorem 8.6): x^p == x (mod p) for ALL x. ---
@given(x=st.integers(min_value=0, max_value=10**6))
@settings(max_examples=300)
def test_fermat_little(x):
    assert pow(x, P, P) == x % P
    assert pow(x, Q, Q) == x % Q


# --- The exact lemma the book reduces to: m | x^{ed} - x for every x. -------
@given(x=st.integers(min_value=0, max_value=10**6))
@settings(max_examples=300)
def test_ed_is_identity_mod_m(x):
    # ed - 1 divisible by (p-1)(q-1) => x^{ed} == x (mod p) and (mod q)
    # => (mod m), since m = p*q with p, q distinct primes.
    assert (pow(x, E * D, M) - x) % M == 0


# --- Full RSA round trip for any plaintext 0 <= x < m. ---------------------
@given(x=st.integers(min_value=0).map(lambda n: n % M))
@settings(max_examples=300)
def test_rsa_round_trip(x):
    r = pow(x, E, M)            # encrypt with public key
    assert pow(r, D, M) == x    # decrypt with private key returns plaintext
