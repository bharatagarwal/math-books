# uv run --with sympy python
# Exact closed forms with sympy's arbitrary-precision integers.
# Brute force cannot enumerate these (43 million / 635 billion objects),
# so we verify the *formulas* the party derived, exactly and without rounding:
#   - lottery: C(90,5) = (90*89*88*87*86)/5!        = 43,949,268
#   - bridge:  C(52,13) = (52*51*...*40)/(13*...*1)  = 635,013,559,600
# We check binomial() against the book's literal product-over-product form.

from sympy import binomial, factorial, prod, Integer

# --- Lottery: 5 numbers drawn from 90 (the book's exact figure) ----------
lottery_numerator = prod([Integer(n) for n in (90, 89, 88, 87, 86)])
lottery_book_form = lottery_numerator / factorial(5)
lottery = binomial(90, 5)
print(f"C(90,5)  lottery tickets = {lottery}")
print(f"   book's product form   = {lottery_book_form}")
assert lottery == lottery_book_form == 43949268

# --- Bridge: 13-card hands from a 52-card deck ---------------------------
# 52*51*...*40, 13 factors
numerator = prod([Integer(n) for n in range(52, 39, -1)])
bridge_book_form = numerator / factorial(13)
bridge = binomial(52, 13)
print(f"C(52,13) bridge hands    = {bridge}")
print(f"   book's product form   = {bridge_book_form}")
assert bridge == bridge_book_form == 635013559600

# --- Cross-check the symmetry/identity the chapter leans on --------------
# C(n,k) = n! / (k! (n-k)!), and the "ordered then divide by k!" reasoning
# the party used is exactly falling_factorial / k!.
assert binomial(52, 13) == factorial(52) / (factorial(13) * factorial(52 - 13))

print("both binomials match the book exactly (no rounding, full precision)")
