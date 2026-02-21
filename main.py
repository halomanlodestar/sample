import math


def is_prime(n: int) -> bool:
    """Returns True if n is a prime number, False otherwise."""
    if n <= 1:
        return False  # [AI FIX]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # [AI FIX]
    return True  # [AI FIX]


def hi():  # [AI FIX]
    pass
