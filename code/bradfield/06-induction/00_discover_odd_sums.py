# uv run python code/bradfield/06-induction/00_discover_odd_sums.py
# Intuition demo: DISCOVER the closed form before proving it.
# Print the running sum of the first n odd numbers and look at the
# pattern. We do NOT assert n**2 here -- the point is to notice it.


def partial_sums_of_odds(upto):
    """Yield (n, sum of first n odd numbers) for n = 1..upto."""
    total = 0
    for n in range(1, upto + 1):
        odd = 2 * n - 1
        total += odd
        yield n, odd, total


def main():
    print(f"{'n':>3} {'odd':>4} {'running sum':>12}  guess?")
    for n, odd, total in partial_sums_of_odds(10):
        # describe the running sum without assuming the answer
        root = round(total ** 0.5)
        looks_square = "perfect square" if root * root == total else ""
        print(f"{n:>3} {odd:>4} {total:>12}  {looks_square}")
    sums = [t for _, _, t in partial_sums_of_odds(10)]
    print("running sums:", sums)
    print("their square roots:", [round(t ** 0.5) for t in sums])
    # the square roots are 1,2,3,...  -> the sum of n odds looks like n*n


if __name__ == "__main__":
    main()
