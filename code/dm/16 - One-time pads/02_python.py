# uv run --with sympy python
# Envelope / bit-commitment scheme (section 16.1, "save the last chess move").
# Alice encodes her move Kf3 -> 1163, extends it to a 200-digit PRIME p whose
# first four digits are 1163, multiplies by a second prime q, and publishes
# only N = p*q.  Easy to verify (test primality, multiply), hard to open
# (factor N) -- exactly the asymmetry the book relies on.
from sympy import nextprime, isprime

MOVE = "Kf3"          # 'K'->11, 'f'->6, '3'->3  ==>  '1163'
move_code = 1163

# --- Alice's commitment ----------------------------------------------------
# Smallest 200-digit prime starting with 1163 = nextprime(1163 * 10^196).
base = 1163 * 10**196
p_smallest = nextprime(base - 1)
print("smallest 1163-prime has 200 digits:", len(str(p_smallest)) == 200)
print("  ...and starts with 1163:         ", str(p_smallest)[:4] == "1163")
# book printed the all-zeros run ending in 371, i.e. base + 371
print("  it is base + ", p_smallest - base)

# The book warns Alice must NOT use the smallest (Bob could guess it); she
# fills the 196 free digits randomly. This is the random 200-digit prime the
# book actually printed -- verify it really is prime and starts with 1163.
p = int(
    "1163146712876555763279909704559660690828365476006668873814489354662"
    "4743604198911046804111038868958805745715572480009569639174033385458"
    "418593535488622323782317577559864739652701127177097278389465414589"
)
print("book's random p: 200 digits, 1163.., prime:",
      len(str(p)) == 200, str(p)[:4] == "1163", isprime(p))

# q: a 201-digit prime; N = p*q is what Alice sends the night before.
q = nextprime(10**200)
N = p * q
print("N has", len(str(N)), "digits")

# --- Next morning: Alice reveals (p, q); Bob verifies and reads the move ---
def verify_and_read(p, q, N):
    assert isprime(p) and isprime(q), "factors must be prime (no cheating)"
    assert p * q == N, "product must equal the committed N"
    smaller = min(p, q)
    return int(str(smaller)[:4])

read_code = verify_and_read(p, q, N)
print("Bob recovers move code:", read_code, "==", move_code,
      "->", read_code == move_code)

# --- Alice cannot swap in a different (p', q') that still multiplies to N ---
# Unique factorization (Theorem 8.1) pins N to exactly {p, q}.
p2 = nextprime(p)       # any other prime
ok = (p2 != p) and (N % p2 != 0)
print("a different prime p' does NOT divide N (binding):", ok)
