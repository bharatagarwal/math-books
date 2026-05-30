# uv run python code/bradfield/01-counting/07_subset_binary_bijection.py
# INTUITION: Lovasz's second proof that a set has 2^n subsets -- the bijection
# subset <-> binary string. Seeing the correspondence laid out is the "aha":
# each element is one bit (in / out), so subsets ARE the numbers 0..2^n - 1.
elements = ["a", "b", "c"]
n = len(elements)

print(f"every subset of {{{','.join(elements)}}} <-> an {n}-bit number\n")
print("  k | bits | subset")
for k in range(2 ** n):
    bits = format(k, f"0{n}b")
    subset = {e for e, b in zip(elements, bits) if b == "1"}
    print(f"  {k} | {bits}  | {sorted(subset) if subset else '{}'}")

# The point: this is a one-to-one correspondence, so #subsets = #numbers = 2^n.
# Reading a subset off a number, and a number off a subset, are inverse maps:
def number_to_subset(k):
    return {e for e, b in zip(elements, format(k, f"0{n}b")) if b == "1"}
def subset_to_number(s):
    return int("".join("1" if e in s else "0" for e in elements), 2)

assert all(subset_to_number(number_to_subset(k)) == k for k in range(2 ** n))
print("\nround-trip number -> subset -> number is the identity: it's a bijection")
