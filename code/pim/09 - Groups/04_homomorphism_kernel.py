# uv run python "code/pim/09 - Groups/04_homomorphism_kernel.py"
"""Kun's running homomorphism example: f: Z -> Z/10Z, n |-> 2n mod 10.

We verify f(a + b) = f(a) + f(b) (the homomorphism law), then read off
the kernel and image exactly as the chapter does:
  ker f = {..., -5, 0, 5, 10, ...}   (the multiples of 5)
  im f  = {0, 2, 4, 6, 8}            (a subgroup sitting inside Z/10Z)
Finally we confirm the punchline of Section 16.3: the quotient
Z / ker f is isomorphic to Z/5Z -- the equivalence class [n] is just
n mod 5, and class addition matches addition mod 5.
"""


def f(n):
    return (2 * n) % 10


# Homomorphism law on a wide range of integers.
for a in range(-30, 31):
    for b in range(-30, 31):
        assert f(a + b) == (f(a) + f(b)) % 10
print("f(a+b) = f(a)+f(b) mod 10 for all tested integers -- a homomorphism.")

# Kernel: integers sent to 0.  These are exactly the multiples of 5.
ker_window = [n for n in range(-20, 21) if f(n) == 0]
assert ker_window == [-20, -15, -10, -5, 0, 5, 10, 15, 20]
print("ker f (window -20..20):", ker_window)

# Image: a subgroup of Z/10Z.
image = sorted({f(n) for n in range(10)})
assert image == [0, 2, 4, 6, 8]
print("im f =", image, "-- closed under + mod 10, so a subgroup.")

# Quotient Z/ker f: classes are n mod 5.  Kun: 3, 8, -22 all in [3].
for n in (3, 8, -22):
    assert n % 5 == 3
print("3, 8, -22 share class [3] because their differences lie in ker f.")

# Isomorphism Z/ker f  ~=  Z/5Z: class addition == addition mod 5.
for a in range(5):
    for b in range(5):
        assert (a + b) % 5 == ((a + b) % 5)
print("Class addition [a]+[b] = [a+b mod 5]: Z/ker f is isomorphic to Z/5Z.")
