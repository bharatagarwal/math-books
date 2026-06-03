# uv run python
# Python's set type IS mathematical set notation.
# Curly braces, membership, operations — the syntax mirrors the math.
A = {1, 2, 3}
B = {2, 4, 6}

print(f"A = {A}")
print(f"B = {B}")
print(f"2 in A: {2 in A}")           # ∈
print(f"5 in A: {5 in A}")           # ∉
print(f"A | B  = {A | B}")           # A ∪ B (union)
print(f"A & B  = {A & B}")           # A ∩ B (intersection)
print(f"A - B  = {A - B}")           # A \ B (difference)
print(f"A ^ B  = {A ^ B}")           # A △ B (symmetric diff)
print(f"|A|    = {len(A)}")          # cardinality
# 2 in A: True
# A | B  = {1, 2, 3, 4, 6}
# A & B  = {2}
# A - B  = {1, 3}
# A ^ B  = {1, 3, 4, 6}
