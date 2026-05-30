# uv run python code/bradfield/02-probability/08_independence_explorer.py
# INTUITION (LL 7.2, Exercise 7.6): independence is not a feeling, it is an
# arithmetic accident -- P(A and B) happening to equal P(A)*P(B). We DISCOVER
# which event pairs are independent by BUILDING the contingency table and
# checking whether the joint cell equals the product of the margins.
from fractions import Fraction
from itertools import combinations

# One fair die: the uniform space S = {1,...,6}, each outcome weight 1/6.
S = list(range(1, 7))


def P(event):
    # Uniform space: probability is just |event| / |S| -- counting / denom.
    return Fraction(len(event), len(S))


# LL's four named events on a die roll.
E = {2, 4, 6}          # even
O = {1, 3, 5}          # odd
T = {3, 6}             # divisible by three
L = {4, 5, 6}          # "better than average" (larger than 3)
named = {"E": E, "O": O, "T": T, "L": L}

# Build the table the book asks us to read off (Exercise 7.6): for every pair,
# compare the JOINT probability P(A & B) against the PRODUCT P(A) P(B).
print(f"{'pair':>6} | {'P(A&B)':>7} | {'P(A)P(B)':>9} | indep? | exclusive?")
print("-" * 52)
independent_pairs = []
for (na, A), (nb, B) in combinations(named.items(), 2):
    joint = P(A & B)
    prod = P(A) * P(B)
    indep = joint == prod
    excl = len(A & B) == 0
    if indep:
        independent_pairs.append(f"{na},{nb}")
    print(f"{na+','+nb:>6} | {str(joint):>7} | {str(prod):>9} |"
          f" {str(indep):>6} | {str(excl):>6}")

# The book's punchline: E and T are independent (E&T = {6}, P = 1/6 = 1/2 * 1/3),
# while E and O are *exclusive* (disjoint) -- and exclusive events with nonzero
# probability are exactly NOT independent (the only overlap is empty).
assert P(E & T) == P(E) * P(T) == Fraction(1, 6)     # the headline example
assert P(E & O) == 0 and P(E) * P(O) != 0            # exclusive => dependent
print("\nindependent pairs:", ", ".join(independent_pairs))
print("E,T independent: P(E&T)=1/6 = (1/2)(1/3); E,O exclusive so dependent.")
