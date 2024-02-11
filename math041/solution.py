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
    prime = 0
    primes = [i for i in range(11, 10000000, 2) if is_prime(i)]
    for i in primes:
        if is_pandigital(i):
            prime = i
    return prime

if __name__ == "__main__":
    print("Math041")
    print("answer() =", answer(), "\n")
