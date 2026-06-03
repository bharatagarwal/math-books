# uv run python
# Boolean operators in Python ARE the logical connectives.
# Math: ∧ → and, ∨ → or, ¬ → not, ⊕ → ^

p, q = True, False

print(f"p = {p}, q = {q}")
print(f"p ∧ q (and):  {p and q}")
print(f"p ∨ q (or):   {p or q}")
print(f"¬p    (not):  {not p}")
print(f"p ⊕ q (xor):  {p ^ q}")
print()

# Truth table for implication (p ⇒ q ≡ ¬p ∨ q)
print("p     | q     | p ⇒ q")
print("------+-------+------")
for p in [True, False]:
    for q in [True, False]:
        implies = (not p) or q
        print(f"{str(p):5} | {str(q):5} | {implies}")
# The only False row: True ⇒ False = False
