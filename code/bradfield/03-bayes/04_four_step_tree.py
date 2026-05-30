# uv run python code/bradfield/03-bayes/04_four_step_tree.py
# DISCOVER the Four-Step Method: build the MCS hockey best-of-three tree, then
# read the conditional probability off the leaves. (MCS ch 18, Fig 18.1)
from fractions import Fraction

# Best-of-three. Win game 1 with prob 1/2. After that: 2/3 if you won the last
# game (invigorated), 1/3 if you lost it (demoralized). Stop at 2 W or 2 L.
WIN_AFTER = {"W": Fraction(2, 3), "L": Fraction(1, 3)}


def grow(history, prob, leaves):
    wins = history.count("W")
    losses = history.count("L")
    if wins == 2 or losses == 2:        # series decided -> leaf
        leaves.append((history, prob))
        return
    # probability of WINNING the next game depends on the previous result
    p_win = Fraction(1, 2) if history == "" else WIN_AFTER[history[-1]]
    grow(history + "W", prob * p_win, leaves)
    grow(history + "L", prob * (1 - p_win), leaves)


# Step 1: build the sample space (every root-to-leaf path) with its probability.
leaves = []
grow("", Fraction(1), leaves)
print("Step 1+3: sample space and outcome probabilities")
for outcome, p in leaves:
    print(f"  {outcome:<3} {p}")
assert sum(p for _, p in leaves) == 1     # a tree's leaves partition all of S

# Step 2: define the events of interest as sets of leaf outcomes.
won_tournament = lambda o: o.count("W") == 2
won_first_game = lambda o: o.startswith("W")


def prob(event):
    return sum(p for o, p in leaves if event(o))


# Step 4: compute the conditional probability by restrict-and-renormalize.
p_first = prob(won_first_game)
p_both = sum(p for o, p in leaves
             if won_first_game(o) and won_tournament(o))
posterior = p_both / p_first
print("\nStep 2+4:")
print("  Pr[win first game]          =", p_first)
print("  Pr[win tournament & first]  =", p_both)
print("  Pr[win tournament | first]  =", posterior, "(MCS: 7/9)")
assert posterior == Fraction(7, 9)
