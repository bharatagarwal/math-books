# uv run python code/bradfield/11-cryptography/02_diffie_hellman.py
"""Diffie-Hellman key exchange (LL ch 16).

Alice and Bob agree on a shared secret over a public channel,
with no prior secret. Security rests on the discrete log problem:
given g, p, and g^a mod p, recovering a is believed hard.
"""
g = 5
p = 23
a = 6   # Alice's secret
b = 15  # Bob's secret

# What travels over the public channel:
A = pow(g, a, p)  # Alice -> Bob
B = pow(g, b, p)  # Bob   -> Alice
print(f"public: g={g} p={p}  Alice sends A={A}  Bob sends B={B}")

# Each raises the other's value to their own secret exponent.
shared_alice = pow(B, a, p)  # (g^b)^a
shared_bob = pow(A, b, p)    # (g^a)^b

# Both land on g^(ab) mod p.
assert shared_alice == shared_bob == pow(g, a * b, p)
print(f"shared secret g^(ab) mod p = {shared_alice}")

# The eavesdropper sees A and B but would need the discrete log.
# Brute force is the only general attack: recover a from g^a.
for guess in range(p):
    if pow(g, guess, p) == A:
        assert guess == a
        break
print(f"discrete log of A={A} base {g}: a={guess}"
      f" (feasible here, infeasible for large p)")
