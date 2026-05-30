# uv run --with sympy python code/bradfield/01-counting/01_rules.py
# Lovasz's party (LL 2.1): the lottery and bridge counts. Both are "ordered
# product, divided by the order we don't care about" -- the division principle.
# Far too large to list, so we check the closed forms exactly with sympy's
# arbitrary-precision integers, the book's form vs. the built-in binomial().
import sympy as sp
from math import factorial

# Lottery: choose 5 numbers from 90. Ordered picks = 90*89*88*87*86; each ticket
# counted 5! times, so divide. LL's figure: 43,949,268.
lottery_ordered = 90 * 89 * 88 * 87 * 86
lottery = lottery_ordered // factorial(5)
assert lottery == int(sp.binomial(90, 5)) == 43_949_268

# Bridge: choose 13 cards from 52. Ordered = 52*51*...*40; each hand counted 13!
# times. LL's figure: 635,013,559,600.
bridge_ordered = 1
for c in range(52, 52 - 13, -1):
    bridge_ordered *= c
bridge = bridge_ordered // factorial(13)
assert bridge == int(sp.binomial(52, 13)) == 635_013_559_600

print("C(90,5)  lottery tickets =", lottery)
print("C(52,13) bridge hands    =", bridge)
print("both match the book; chance of the same bridge hand twice = 1 in", bridge)
