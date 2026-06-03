# uv run python
"""
Python number types and their mathematical counterparts.

Math set        Python type     Example
---------       -----------     -------
N (naturals)    int (>= 0)     0, 1, 2, ...
Z (integers)    int             ..., -2, -1, 0, 1, 2, ...
Q (rationals)   Fraction        1/3, -7/4
R (reals)       float           3.14159...
C (complex)     complex         2 + 3j
"""
from fractions import Fraction

# --- The number-set tower: N c Z c Q c R c C ---

n: int = 7              # natural (N): non-negative int
z: int = -3             # integer (Z)
q: Fraction = Fraction(22, 7)  # rational (Q)
r: float = 3.14159      # real (R) -- approximate
c: complex = 2 + 3j     # complex (C) -- j is Python's i

print("=== Number types ===")
print(f"N:  {n}  type={type(n).__name__}")
print(f"Z:  {z}  type={type(z).__name__}")
print(f"Q:  {q}  type={type(q).__name__}")
print(f"R:  {r}  type={type(r).__name__}")
print(f"C:  {c}  type={type(c).__name__}")

# Python's int has arbitrary precision -- no overflow
big = 2**100
print(f"\n2^100 = {big}")
print(f"  ({big.bit_length()} bits, type={type(big).__name__})")

# --- Complex arithmetic ---
print("\n=== Complex arithmetic ===")
w = 1 + 2j
z2 = 3 - 1j
print(f"w = {w},  z = {z2}")
print(f"w + z = {w + z2}")
print(f"w * z = {w * z2}")

# |z| = sqrt(a^2 + b^2)  -- absolute value / magnitude
print(f"|w|   = {abs(w):.4f}")

# conjugate: a + bi -> a - bi
print(f"conj(w) = {w.conjugate()}")

# Real and imaginary parts: Re(z), Im(z)
print(f"Re(w) = {w.real},  Im(w) = {w.imag}")

# --- isinstance checks for set membership ---
print("\n=== Set membership checks ===")


def in_naturals(x):
    """x in N: non-negative integer."""
    return isinstance(x, int) and x >= 0


def in_integers(x):
    """x in Z: any integer."""
    return isinstance(x, int)


def in_rationals(x):
    """x in Q: int or Fraction."""
    return isinstance(x, (int, Fraction))


vals = [0, -3, Fraction(1, 3), 3.14, 2 + 1j]
for v in vals:
    print(
        f"  {str(v):>10}:  "
        f"N={str(in_naturals(v)):<5}  "
        f"Z={str(in_integers(v)):<5}  "
        f"Q={in_rationals(v)}"
    )

# Output:
# === Number types ===
# N:  7  type=int
# Z:  -3  type=int
# Q:  22/7  type=Fraction
# R:  3.14159  type=float
# C:  (2+3j)  type=complex
#
# 2^100 = 1267650600228229401496703205376
#   (101 bits, type=int)
#
# === Complex arithmetic ===
# w = (1+2j),  z = (3-1j)
# w + z = (4+1j)
# w * z = (5+5j)
# |w|   = 2.2361
# conj(w) = (1-2j)
# Re(w) = 1.0,  Im(w) = 2.0
#
# === Set membership checks ===
#            0:  N=True   Z=True   Q=True
#           -3:  N=False  Z=True   Q=True
#          1/3:  N=False  Z=False  Q=True
#         3.14:  N=False  Z=False  Q=False
#       (2+1j):  N=False  Z=False  Q=False
