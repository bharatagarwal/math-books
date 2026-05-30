# uv run python code/bradfield/11-cryptography/04_euler_decryption.py
"""WHY Euler's theorem makes RSA decryption invert encryption.

Intuition demo on LL's example (p=5, q=11, n=55, e=3, d=27).
We do NOT just assert c^d == m; we EXHIBIT the mechanism:

  1. Euler: m^phi(n) == 1 (mod n) for gcd(m, n)=1.
  2. d*e = 1 + t*phi, so c^d = m^(d*e) = m * (m^phi)^t == m * 1^t.
  3. Then we hand-trace 13^27 mod 55 by repeated squaring, the way
     LL does it on the page, so the abstract proof becomes arithmetic.
"""

p, q, e, d = 5, 11, 3, 27
n = p * q
phi = (p - 1) * (q - 1)
m = 7
c = pow(m, e, n)
print(f"n={n} phi={phi} e={e} d={d}  message m={m} ciphertext c={c}")

# Step 1: Euler's theorem on this modulus.
assert pow(m, phi, n) == 1
print(f"Euler: m^phi = {m}^{phi} mod {n} = {pow(m, phi, n)}  (== 1)")

# Step 2: d*e is 1 plus a multiple of phi, so the exponent on m
# collapses by Euler's theorem.
t, r = divmod(d * e, phi)
assert r == 1
print(f"d*e = {d*e} = {t}*phi + 1, so c^d = m^(d*e)"
      f" = m * (m^phi)^{t} == m * 1^{t} = m")
assert pow(c, d, n) == pow(m, d * e, n) == m

# Step 3: hand-trace 13^27 mod 55 by repeated squaring (LL's trace).
# 27 = 16 + 8 + 2 + 1.
powers = {}
cur, exp = c, 1
while exp <= 16:
    powers[exp] = cur
    cur = (cur * cur) % n
    exp *= 2
print("repeated squaring of c=13 mod 55:")
for exp in (1, 2, 4, 8, 16):
    print(f"  13^{exp:<2} = {powers[exp]}")
assert (powers[2], powers[4], powers[8], powers[16]) == (4, 16, 36, 31)

acc = 1
for exp in (16, 8, 2, 1):       # 16 + 8 + 2 + 1 = 27
    acc = (acc * powers[exp]) % n
print(f"13^27 = 13^16 * 13^8 * 13^2 * 13^1 mod 55 = {acc}")
assert acc == m  # back to the original message, 7
print(f"decryption recovers m = {acc}")
