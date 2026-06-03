# uv run --with sympy python
"""
SymPy for number theory notation: intervals, floor/ceiling,
modular arithmetic, famous constants, and number sets.
"""
import sympy as sp
from sympy import (
    S, oo, pi, E, GoldenRatio, EulerGamma,
    floor, ceiling, Mod, Rational, I,
    Interval, FiniteSet, sqrt, simplify,
    isprime, factorint,
)

x = sp.Symbol('x')

# --- Number sets: SymPy knows them ---
print("=== SymPy number sets ===")
print(f"  7 in Naturals?   {7 in S.Naturals}")
print(f" -3 in Integers?   {-3 in S.Integers}")
print(f"1/3 in Rationals?  {Rational(1, 3) in S.Rationals}")
print(f" pi in Reals?      {pi in S.Reals}")
print(f"  i in Complexes?  {I in S.Complexes}")
print(f"  7 in Reals?      {7 in S.Reals}")

# --- Intervals: [a,b], (a,b), [a,b), (a,b] ---
print("\n=== Intervals ===")
closed = Interval(1, 5)          # [1, 5]
open_iv = Interval.open(1, 5)    # (1, 5)
half = Interval(1, 5, False, True)  # [1, 5)
inf_iv = Interval(0, oo)        # [0, inf)

print(f"  [1,5]   = {closed}")
print(f"  (1,5)   = {open_iv}")
print(f"  [1,5)   = {half}")
print(f"  [0,oo)  = {inf_iv}")
print(f"  3 in [1,5]?  {3 in closed}")
print(f"  5 in [1,5)?  {5 in half}")

# Interval arithmetic
A = Interval(1, 3)
B = Interval(2, 5)
print(f"\n  A = {A},  B = {B}")
print(f"  A union B     = {A.union(B)}")
print(f"  A intersect B = {A.intersect(B)}")

# --- Floor and ceiling ---
print("\n=== Floor and ceiling ===")
vals = [Rational(7, 2), Rational(-7, 2), pi]
for v in vals:
    f, c = floor(v), ceiling(v)
    print(f"  floor({v}) = {f},  ceil({v}) = {c}")

# --- Modular arithmetic ---
print("\n=== Modular arithmetic (mod) ===")
# In math: a mod n, or a (mod n)
# Python:  a % n
# SymPy:   Mod(a, n)
print(f"  17 mod 5  = {Mod(17, 5)}")
print(f"  -3 mod 7  = {Mod(-3, 7)}")
print(f"  Symbolic:  Mod(x**2 + 3, 5) = {Mod(x**2 + 3, 5)}")

# Z_n = {0, 1, ..., n-1} with operations mod n
n = 7
Zn = FiniteSet(*range(n))
print(f"\n  Z_{n} = {Zn}")

# Multiplication table mod 3 (compact)
print("  Z_3 multiplication:")
for a in range(3):
    row = [Mod(a * b, 3) for b in range(3)]
    print(f"    {a}: {row}")

# --- Famous constants ---
print("\n=== Famous constants (to 15 digits) ===")
consts = {
    'e (Euler)': E,
    'pi': pi,
    'gamma (Euler-Mascheroni)': EulerGamma,
    'phi (golden ratio)': GoldenRatio,
}
for name, const in consts.items():
    print(f"  {name:30s} = {sp.N(const, 15)}")

# Verify golden ratio: phi = (1 + sqrt(5)) / 2
phi_formula = (1 + sqrt(5)) / 2
print(f"\n  phi == (1+sqrt(5))/2?  "
      f"{simplify(GoldenRatio - phi_formula) == 0}")

# Euler's identity: e^(i*pi) + 1 = 0
euler_id = sp.exp(I * pi) + 1
print(f"  e^(i*pi) + 1 = {simplify(euler_id)}")

# --- Bonus: number theory helpers ---
print("\n=== Number theory ===")
print(f"  isprime(17)    = {isprime(17)}")
print(f"  isprime(18)    = {isprime(18)}")
print(f"  factorint(360) = {factorint(360)}")

# Output:
# === SymPy number sets ===
#   7 in Naturals?   True
#  -3 in Integers?   True
# 1/3 in Rationals?  True
#  pi in Reals?      True
#   i in Complexes?  True
#   7 in Reals?      True
#
# === Intervals ===
#   [1,5]   = Interval(1, 5)
#   (1,5)   = Interval.open(1, 5)
#   [1,5)   = Interval.Ropen(1, 5)
#   [0,oo)  = Interval(0, oo)
#   3 in [1,5]?  True
#   5 in [1,5)?  False
#
#   A = Interval(1, 3),  B = Interval(2, 5)
#   A union B     = Interval(1, 5)
#   A intersect B = Interval(2, 3)
#
# === Floor and ceiling ===
#   floor(7/2) = 3,  ceil(7/2) = 4
#   floor(-7/2) = -4,  ceil(-7/2) = -3
#   floor(pi) = 3,  ceil(pi) = 4
#
# === Modular arithmetic (mod) ===
#   17 mod 5  = 2
#   -3 mod 7  = 4
#   Symbolic:  Mod(x**2 + 3, 5) = Mod(x**2 + 3, 5)
#
#   Z_7 = {0, 1, 2, 3, 4, 5, 6}
#   Z_3 multiplication:
#     0: [0, 0, 0]
#     1: [0, 1, 2]
#     2: [0, 2, 1]
#
# === Famous constants (to 15 digits) ===
#   e (Euler)                      = 2.71828182845905
#   pi                             = 3.14159265358979
#   gamma (Euler-Mascheroni)       = 0.577215664901533
#   phi (golden ratio)             = 1.61803398874989
#
#   phi == (1+sqrt(5))/2?  True
#   e^(i*pi) + 1 = 0
#
# === Number theory ===
#   isprime(17)    = True
#   isprime(18)    = False
#   factorint(360) = {2: 3, 3: 2, 5: 1}
