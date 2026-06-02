# uv run python "code/pim/03 - Sets/03_tournament.py"
# The clever-bijection argument: in a single-elimination tournament
# of n players, the map (game -> loser of that game) is a bijection
# onto the set of losers, and exactly one player never loses. So the
# number of games is n - 1, for ANY n -- no edge-case bookkeeping.
import random


def run_tournament(n, seed=0):
    """Play a single-elimination tournament; return the game count."""
    rng = random.Random(seed)
    players = list(range(n))
    games = 0
    losers = []
    while len(players) > 1:
        rng.shuffle(players)
        survivors = []
        # Pair players off; an odd one out sits the round.
        for i in range(0, len(players) - 1, 2):
            a, b = players[i], players[i + 1]
            winner, loser = (a, b) if rng.random() < 0.5 else (b, a)
            survivors.append(winner)
            losers.append(loser)
            games += 1
        if len(players) % 2 == 1:
            survivors.append(players[-1])
        players = survivors
    champion = players[0]
    return games, losers, champion


# Kun's own example: a thousand players give 999 games.
games, losers, champ = run_tournament(1000, seed=42)
assert games == 999
# loser-map is a bijection onto losers; every non-champion loses once.
assert len(losers) == len(set(losers))          # injective
assert champ not in losers                       # the lone winner
assert set(losers) == set(range(1000)) - {champ}
print(f"1000 players -> {games} games (one less than the players)")

# The pattern holds for every size and every random draw.
for n in [1, 2, 3, 7, 16, 17, 50, 128, 333]:
    for seed in range(5):
        g, _, _ = run_tournament(n, seed=seed)
        assert g == n - 1
print("verified: n players always produce n - 1 games")
