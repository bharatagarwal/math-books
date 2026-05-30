# uv run python code/bradfield/06-induction/02_strong_induction.py
# STRONG induction: P(n) may lean on ALL smaller cases, not just P(n-1).
# Classic example (the "Chicken McNugget" / Frobenius problem): every integer
# amount >= 8 can be paid with 3- and 5-unit coins.

def representable_upto(N, coins=(3, 5)):
    ok = [False] * (N + 1)
    ok[0] = True  # zero is payable with no coins
    for t in range(1, N + 1):
        ok[t] = any(t - c >= 0 and ok[t - c] for c in coins)
    return ok

ok = representable_upto(1000)

# The theorem: representable for every n >= 8.
assert all(ok[n] for n in range(8, 1001))

# It is tight: 1, 2, 4, 7 are NOT representable (7 is the Frobenius number of 3,5).
assert not any(ok[n] for n in (1, 2, 4, 7))

# The strong-induction structure made explicit. Base cases 8, 9, 10 = 3+5, 3+3+3,
# 5+5. For n >= 11, reduce by a 3-coin: n is representable BECAUSE n-3 is. That
# step needs P(n-3), a case far below P(n-1) -- which is why we need *strong*
# induction here.
assert ok[8] and ok[9] and ok[10]
assert all(ok[n - 3] and ok[n] for n in range(11, 1001))

print("every amount >= 8 is payable with 3s and 5s; 1,2,4,7 are not")
print("strong step verified: ok[n] follows from ok[n-3] for all n >= 11")
