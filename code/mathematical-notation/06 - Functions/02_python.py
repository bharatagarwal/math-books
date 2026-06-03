# uv run --with sympy python
# Standard functions: notation <-> Python/SymPy mapping.
# Every function in math notation has a code counterpart.
import math
import sympy as sp

x = sp.Symbol('x')

# --- Trig: sin, cos, tan and inverses ---
print("=== Trigonometric functions ===")
print(f"sin(pi/6) = {math.sin(math.pi/6):.4f}")
print(f"cos(pi/3) = {math.cos(math.pi/3):.4f}")
print(f"sin⁻¹(0.5) = arcsin(0.5) = "
      f"{math.asin(0.5):.4f} rad "
      f"= pi/{int(math.pi/math.asin(0.5))}")
# SymPy: exact symbolic values
print(f"SymPy: sin(pi/6) = {sp.sin(sp.pi/6)}")

# --- Exponential and logarithm ---
print("\n=== exp and log ===")
print(f"exp(1) = e = {math.exp(1):.6f}")
print(f"ln(e)  = log_e(e)  = {math.log(math.e):.1f}")
print(f"log10(1000)         = {math.log10(1000):.1f}")
print(f"log2(1024) = lg(1024) = {math.log2(1024):.1f}")
# Notation:  ln x = log_e x   (math.log)
#            lg x = log_2 x   (math.log2)
#           log x = ambiguous! (base 10 or e)

# --- Floor and ceiling ---
print("\n=== floor and ceiling ===")
vals = [2.3, -1.7, 3.0, math.e, math.pi]
for v in vals:
    print(f"  floor({v:5.2f}) = {math.floor(v):3d}"
          f"   ceil({v:5.2f}) = {math.ceil(v):3d}")
# ⌊e⌋ = ⌈3⌉ = ⌊3⌋ = ⌊pi⌋ = 3

# --- Signum (sgn) ---
print("\n=== sgn ===")
for v in [5, 0, -3]:
    sgn = (v > 0) - (v < 0)
    print(f"  sgn({v:3d}) = {sgn}")

# --- Hyperbolic functions ---
print("\n=== Hyperbolic ===")
print(f"sinh(1) = (e - e⁻¹)/2 = {math.sinh(1):.6f}")
print(f"cosh(1) = (e + e⁻¹)/2 = {math.cosh(1):.6f}")

# --- Gamma and factorial ---
print("\n=== Gamma and factorial ===")
print(f"5! = {math.factorial(5)}")
print(f"Gamma(6) = 5! = {math.gamma(6):.1f}")
print(f"Gamma(0.5) = sqrt(pi) = "
      f"{math.gamma(0.5):.6f} "
      f"≈ {math.sqrt(math.pi):.6f}")
