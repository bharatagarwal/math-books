# uv run --with numpy python code/bradfield/03-bayes/03_monty_hall.py
# Monty Hall: switching wins 2/3 of the time. Bayes made visceral by simulation.
# This is the MCS 18.1 opening example, now resolved correctly.
from fractions import Fraction
import numpy as np

# Exact a posteriori probability via Bayes. Pick door A; Monty opens B (goat).
# Hypotheses: car behind A, B, or C, each prior 1/3.
# Likelihood = Pr[Monty opens B | car location], given he never opens your door
# or the car: if car at A he picks B or C at random (1/2); if car at C he MUST
# open B (1); if car at B he can't open B (0).
prior = {"A": Fraction(1, 3), "B": Fraction(1, 3), "C": Fraction(1, 3)}
like = {"A": Fraction(1, 2), "B": Fraction(0), "C": Fraction(1)}
evidence = sum(prior[h] * like[h] for h in prior)        # Pr[Monty opens B]
post = {h: prior[h] * like[h] / evidence for h in prior}
print("posterior after Monty opens B (you picked A):")
for h in "ABC":
    print(f"  car at {h}: {post[h]}")
assert post["A"] == Fraction(1, 3)   # staying wins 1/3
assert post["C"] == Fraction(2, 3)   # switching (to C) wins 2/3

rng = np.random.default_rng(42)
trials = 1_000_000

car = rng.integers(0, 3, size=trials)      # door hiding the car
pick = rng.integers(0, 3, size=trials)     # contestant's first pick

# Strategy 1: STAY. You win exactly when your first pick was right -> 1/3.
stay_wins = (pick == car).mean()

# Strategy 2: SWITCH. Monty opens a goat door; you switch to the other one.
# You win whenever your first pick was WRONG (the remaining door is the car).
switch_wins = (pick != car).mean()

assert abs(stay_wins - 1 / 3) < 0.005
assert abs(switch_wins - 2 / 3) < 0.005
assert abs((stay_wins + switch_wins) - 1.0) < 1e-9  # strategies partition

print("\nstay   wins:", round(stay_wins, 4), "(~1/3)")
print("switch wins:", round(switch_wins, 4), "(~2/3)")
