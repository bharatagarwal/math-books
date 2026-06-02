# uv run python "code/pim/03 - Sets/05_stable_marriage.py"
# Gale-Shapley deferred acceptance, faithful to Kun's Suitor/Suited
# classes. We run his exact example, then verify two theorems:
#   (1) the output matching is STABLE -- no blocking pair, and
#   (2) it is SUITOR-OPTIMAL -- every suitor gets the best partner
#       he could have in ANY stable matching (proposer-optimality).
from itertools import permutations


class Suitor:
    def __init__(self, id, preference_list):
        self.preference_list = preference_list
        self.index_to_propose_to = 0
        self.id = id

    def preference(self):
        return self.preference_list[self.index_to_propose_to]

    def post_rejection(self):
        self.index_to_propose_to += 1


class Suited:
    def __init__(self, id, preference_list):
        self.preference_list = preference_list
        self.held = None
        self.current_suitors = set()
        self.id = id

    def reject(self):
        if len(self.current_suitors) == 0:
            return set()
        self.held = min(
            self.current_suitors,
            key=lambda s: self.preference_list.index(s.id))
        rejected = self.current_suitors - set([self.held])
        self.current_suitors = set([self.held])
        return rejected

    def add_suitor(self, suitor):
        self.current_suitors.add(suitor)


def stable_marriage(suitors, suiteds):
    unassigned = set(suitors)
    while len(unassigned) > 0:
        for suitor in unassigned:
            target = suiteds[suitor.preference()]
            target.add_suitor(suitor)
        unassigned = set()
        for suited in suiteds:
            unassigned |= suited.reject()
        for suitor in unassigned:
            suitor.post_rejection()
    return {suited.held.id: suited.id for suited in suiteds}


def is_stable(match, suitor_pref, suited_pref):
    """match: suitor_id -> suited_id. Check for any blocking pair."""
    partner_of_suited = {w: m for m, w in match.items()}
    for m, w in match.items():
        for w2 in suitor_pref[m]:
            if w2 == w:
                break  # m likes w at least as much as w2
            m2 = partner_of_suited[w2]
            # w2 prefers m over her current partner m2?
            if suited_pref[w2].index(m) < suited_pref[w2].index(m2):
                return False  # (m, w2) is a blocking pair
    return True


def all_stable_matchings(suitor_pref, suited_pref):
    """Brute force every perfect matching, keep the stable ones."""
    n = len(suitor_pref)
    stable = []
    for perm in permutations(range(n)):
        match = {m: perm[m] for m in range(n)}
        if is_stable(match, suitor_pref, suited_pref):
            stable.append(match)
    return stable


# ---- Kun's example run -------------------------------------------
suitor_pref = {
    0: [3, 5, 4, 2, 1, 0],
    1: [2, 3, 1, 0, 4, 5],
    2: [5, 2, 1, 0, 3, 4],
    3: [0, 1, 2, 3, 4, 5],
    4: [4, 5, 1, 2, 0, 3],
    5: [0, 1, 2, 3, 4, 5],
}
suited_pref = dict(suitor_pref)  # same lists, per the book's example

suitors = [Suitor(i, list(suitor_pref[i])) for i in range(6)]
suiteds = [Suited(i, list(suited_pref[i])) for i in range(6)]
match = stable_marriage(suitors, suiteds)

print("matching (suitor -> suited):")
for m in sorted(match):
    print(f"  Suitor({m}) -> Suited({match[m]})")

# Theorem 4.15: the deferred-acceptance output is stable.
assert is_stable(match, suitor_pref, suited_pref)
print("no blocking pair: the matching is STABLE")

# Proposer-optimality: each suitor's partner is his best possible
# across the set of ALL stable matchings.
stable_set = all_stable_matchings(suitor_pref, suited_pref)
assert match in stable_set
for m in range(6):
    best_rank = min(suitor_pref[m].index(s[m]) for s in stable_set)
    assert suitor_pref[m].index(match[m]) == best_rank
print(f"found {len(stable_set)} stable matchings total;")
print("deferred acceptance gives each SUITOR his optimal one")

# Sanity: with the symmetric "everyone agrees" preferences above,
# stability is a strong constraint -- check a randomized instance too.
import random
rng = random.Random(7)
n = 5
sp = {i: rng.sample(range(n), n) for i in range(n)}
tp = {i: rng.sample(range(n), n) for i in range(n)}
S = [Suitor(i, list(sp[i])) for i in range(n)]
T = [Suited(i, list(tp[i])) for i in range(n)]
rmatch = stable_marriage(S, T)
assert is_stable(rmatch, sp, tp)
print("random 5x5 instance also yields a stable matching")
