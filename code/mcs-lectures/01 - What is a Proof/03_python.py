# Multiplication is trivial; factoring is hard
from sympy import nextprime, factorint
import time

p = nextprime(10**50)
q = nextprime(10**50 + 10**40)
N = p * q  # instant

print(f"N has {len(str(N))} digits")
# Factoring N back to p,q would take years for cryptographic sizes
