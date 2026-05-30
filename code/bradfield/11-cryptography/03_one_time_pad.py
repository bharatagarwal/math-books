# uv run python code/bradfield/11-cryptography/03_one_time_pad.py
"""One-time pad perfect secrecy, shown by enumeration (LL ch 16).

Intuition demo: encode messages as 3-bit strings. With a uniformly
random 3-bit key, c = m XOR k. We DISCOVER perfect secrecy by
building the full table: for any fixed ciphertext c, every message
m is reached by exactly one key, so P(m | c) is the same for all m.
Then we show why reuse breaks it: c1 XOR c2 = m1 XOR m2.
"""
from itertools import product
from collections import defaultdict

N = 3
msgs = ["".join(b) for b in product("01", repeat=N)]
keys = msgs  # same space: all 3-bit strings


def xor(x, y):
    return "".join("1" if a != b else "0" for a, b in zip(x, y))


# Build the (message, key) -> ciphertext table and group by
# ciphertext: which (m, k) pairs produce each c?
by_cipher = defaultdict(list)
for m in msgs:
    for k in keys:
        by_cipher[xor(m, k)].append((m, k))

# Perfect secrecy: fix any ciphertext. Every message appears
# exactly once among the keys that yield it, so seeing c tells
# the eavesdropper nothing -- all messages stay equally likely.
print("ciphertext  ->  (message, key) pairs that produce it")
for c in msgs:
    pairs = by_cipher[c]
    reached = sorted(m for m, _ in pairs)
    print(f"  {c}  ->  {pairs}")
    assert reached == sorted(msgs)  # every message, exactly once
print("for every ciphertext, each message reachable by exactly"
      " one key: P(m | c) is uniform -> perfect secrecy")

# The other half of LL's point: the key must be used ONCE.
# Reuse the same key on two messages and the key cancels.
k = "101"
m1, m2 = "110", "011"
c1, c2 = xor(m1, k), xor(m2, k)
leak = xor(c1, c2)
print(f"\nkey reuse: c1 XOR c2 = {leak} = m1 XOR m2 ="
      f" {xor(m1, m2)} (key cancels, leaks the difference)")
assert leak == xor(m1, m2)
