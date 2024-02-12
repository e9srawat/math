"""Pandigital Prime"""


def is_prime(num):
    """returns true if num is prime else false"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_pandigital(num):
    """returns true if num is pandigital else false"""
    for i in range(1, len(str(num)) + 1):
        if str(i) not in str(num):
            return False
    return True


def answer():
    """answer function"""
    primes = [i for i in range(7000000, 8000000) if is_prime(i)]
    for i in primes[::-1]:
        if is_pandigital(i):
            return i
    return None


if __name__ == "__main__":
    print("Math041")
    print("answer() =", answer(), "\n")
