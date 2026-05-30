# uv run python
# One-time pad (section 16) + why reuse is fatal (exercise 16.3).
# Reproduces the book's EXACT pad/plaintext/ciphertext bit strings,
# then shows that XORing two messages encrypted under the SAME pad
# cancels the pad and leaks plaintext1 XOR plaintext2.
import textwrap


def xor_bits(a, b):
    """Bitwise XOR of two equal-length 0/1 strings (the pad's '+' mod 2)."""
    assert len(a) == len(b)
    return "".join("1" if x != y else "0" for x, y in zip(a, b))


def encode(msg):
    """Book's encoding: A=00001, ..., Z=11010, Space=00000, 5 bits each."""
    out = ""
    for c in msg:
        n = 0 if c == " " else ord(c) - ord("A") + 1
        out += format(n, "05b")
    return out


def decode(bits):
    out = ""
    for g in textwrap.wrap(bits, 5):
        n = int(g, 2)
        out += " " if n == 0 else chr(ord("A") + n - 1)
    return out


# ---- 1. Reproduce the book's exact example (section 16) -------------------
PAD = "11000111000010000110010100100100101100110010101100001110110000010"
BOOK_PLAIN = "00001100101001000001000110101100000011010111101110001000000111001"
BOOK_CIPH = "11001011101011000111010010001000101111100101000010000110110111011"

# Arthur encrypts: ciphertext = plaintext XOR pad (he "flips" the marked bits)
ciph = xor_bits(BOOK_PLAIN, PAD)
print("encrypt reproduces book ciphertext:", ciph == BOOK_CIPH)

# Bela decrypts: XOR the same pad back -> original plaintext
recovered = xor_bits(ciph, PAD)
print("decrypt round-trips to plaintext: ", recovered == BOOK_PLAIN)

# ---- 2. A clean send of "ATTACK MONDAY" with the book's method ------------
m1 = encode("ATTACK MONDAY")
# 65-bit pad (one bit per plaintext bit)
pad1 = ("01101001100101101001011010010110"
        "100101101001011010010110100101101")
c1 = xor_bits(m1, pad1)
round_trip = decode(xor_bits(c1, pad1)) == "ATTACK MONDAY"
print("ATTACK MONDAY round-trip:        ", round_trip)

# ---- 3. Why reuse is fatal (exercise 16.3) --------------------------------
# Bela reuses the SAME pad for a second message of the same length.
m2 = encode("RETREAT FRIDAY")[: len(pad1)]  # trim to pad length
c2 = xor_bits(m2, pad1)

# Caligula intercepts c1 and c2. He cannot get the pad, but XORing the two
# ciphertexts cancels it entirely:  c1 XOR c2 = (m1^pad)^(m2^pad) = m1 XOR m2.
leak = xor_bits(c1, c2)
print("c1 XOR c2 == m1 XOR m2 (pad gone):", leak == xor_bits(m1, m2))
print("leaked m1 XOR m2 (no key needed): ", leak)
