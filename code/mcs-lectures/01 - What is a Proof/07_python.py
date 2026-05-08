def is_prime(n: int) -> bool:
    if n < 2: return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0: return False
    return True

# is_prime(7) = True   (a true proposition)
# is_prime(8) = False  (a false proposition)
