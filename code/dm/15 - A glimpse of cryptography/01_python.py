# uv run python
"""Section 15.1 — why a substitution cipher is weak. It only RELABELS letters,
so it leaves the frequency pattern intact, and an attacker who knows English
letter frequencies can recover the key with no key material. Pure stdlib."""
import random
import string
from collections import Counter

PLAIN = (
    "the science of secret communication is older than the printing press. "
    "for centuries a message was hidden by replacing each letter of the "
    "alphabet with another letter, a scheme we now call a substitution "
    "cipher. it looks scrambled to the naked eye, yet it leaks far more than "
    "its users had hoped. because every occurrence of a given letter is "
    "always replaced by the same symbol, the count of how often each symbol "
    "appears is left completely intact. and in ordinary english the letter e "
    "is far more common than any other, followed by t, then a, o, i and n. "
    "so an eavesdropper merely tallies the symbols and lines those counts up "
    "against the known letter frequencies of english to recover the message."
)
ALPHA = string.ascii_lowercase


def apply_key(text, key):
    return "".join(key.get(ch, ch) for ch in text)


key = dict(zip(ALPHA, random.Random(7).sample(ALPHA, len(ALPHA))))
inverse = {v: k for k, v in key.items()}
cipher = apply_key(PLAIN, key)

# 1. A substitution cipher is a bijection: the true key decrypts exactly.
assert apply_key(cipher, inverse) == PLAIN
print("round-trip with the true key is lossless:", True)

# 2. It only relabels letters, so the multiset of letter counts is unchanged --
#    precisely the leak that frequency analysis exploits.
def profile(s):
    return sorted(Counter(c for c in s if c.isalpha()).values(), reverse=True)


assert profile(PLAIN) == profile(cipher)
print("plaintext and ciphertext share an identical frequency profile:", True)

# 3. The attack, using NO key material: rank the cipher symbols by frequency and
#    map them onto the standard English frequency order.
ENGLISH = "etaoinshrdlcumwfgypbvkjxqz"
ranked = [s for s, _ in Counter(c for c in cipher if c.isalpha()).most_common()]
guess = {sym: ENGLISH[i] for i, sym in enumerate(ranked)}
recovered = apply_key(cipher, guess)

hits = sum(a == b for a, b in zip(PLAIN, recovered) if a.isalpha())
total = sum(c.isalpha() for c in PLAIN)
pct = hits / total
print(f"letters recovered by frequency alone: {hits}/{total} = {pct:.0%}")
print("first line recovered with no key:\n  " + recovered[:66])
assert hits / total > 0.2  # vastly better than the ~1/26 expected by chance
