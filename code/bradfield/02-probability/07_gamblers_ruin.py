# uv run --with numpy python code/bradfield/02-probability/07_gamblers_ruin.py
# LL 7.4: Gambler's Ruin. A starts with $a, B with $b, fair coin each round,
# play till someone is broke. Claim: P(A takes everything) = a/(a+b).
# LL gives a slick argument: the game is fair, so A's EXPECTED final fortune
# equals the starting a. The final fortune is (a+b) with prob q, else 0, so
# q(a+b) = a  =>  q = a/(a+b). We confirm that by simulation.
import numpy as np

def simulate(a, b, trials, rng):
    wins = 0
    total = a + b
    for _ in range(trials):
        fortune = a
        while 0 < fortune < total:
            fortune += 1 if rng.random() < 0.5 else -1
        if fortune == total:
            wins += 1
    return wins / trials

rng = np.random.default_rng(1)
for a, b in [(5, 10), (1, 1), (3, 7), (8, 2)]:
    q_theory = a / (a + b)
    q_sim = simulate(a, b, 4000, rng)
    assert abs(q_sim - q_theory) < 0.04
    print(f"a={a:>2}, b={b:>2}:  a/(a+b) = {q_theory:.3f}   simulated = {q_sim:.3f}")

# The moral (LL): against a much richer opponent, even a FAIR game ruins you
# with high probability -- a=1 vs b=999 means you win only 1 time in 1000.
print("\nfair game, a=1 vs b=999: P(you win it all) =", 1 / (1 + 999))
