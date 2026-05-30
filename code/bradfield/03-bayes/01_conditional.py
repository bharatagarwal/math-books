# uv run python code/bradfield/03-bayes/01_conditional.py
# Conditioning = shrinking the sample space to the outcomes now known to occur.
# Definition (MCS 18.2): Pr[X | Y] = Pr[X and Y] / Pr[Y].
from itertools import product
from fractions import Fraction

# The "two children" puzzle. A family has two kids, each equally likely B/G.
omega = list(product("BG", repeat=2))   # BB, BG, GB, GG -- 4 equally likely


def P(event):
    return Fraction(sum(1 for o in omega if event(o)), len(omega))


def Pcond(event, given):
    # P(event | given) = P(event and given) / P(given): restrict, then count.
    num = sum(1 for o in omega if given(o) and event(o))
    den = sum(1 for o in omega if given(o))
    return Fraction(num, den)


both_boys = lambda o: o == ("B", "B")
at_least_one_boy = lambda o: "B" in o
older_is_boy = lambda o: o[0] == "B"

# "At least one boy" -> P(both boys) = 1/3, NOT 1/2. The condition keeps three
# equally likely outcomes {BB, BG, GB}; only one is BB.
assert Pcond(both_boys, at_least_one_boy) == Fraction(1, 3)

# But "the OLDER is a boy" -> P(both boys) = 1/2. A different condition, a
# different restricted space {BB, BG}. Which fact you learn changes the answer.
assert Pcond(both_boys, older_is_boy) == Fraction(1, 2)

print("P(both boys | at least one boy) =", Pcond(both_boys, at_least_one_boy))
print("P(both boys | older is a boy)  =", Pcond(both_boys, older_is_boy))

# This is exactly the MCS 18.1 Monty Hall confusion: conditioning on a SLOPPY
# event ("a goat is behind B") instead of the PRECISE event you witnessed
# ("Monty OPENED B") silently folds in an extra outcome and gives the wrong
# answer 1/2 instead of 2/3. Same lesson, life-sized: be exact about the given.
print("\nSame trap powers the Monty Hall paradox: condition on what you")
print("actually observed, not a looser event that happens to be implied.")
