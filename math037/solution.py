"""Truncatable Primes"""


def is_prime(num):
    """finds if num is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_trunc(num):
    """finds if num is truncatable from left to right and right to left"""
    num = list(str(num))
    for i in range(1, len(num)):
        if not is_prime(int("".join(num[:-i]))):
            return False
        if not is_prime(int("".join(num[i:]))):
            return False
    return True


def answer():
    """answer function"""
    primes = [i for i in range(11, 1000000, 2) if is_prime(i)]
    return sum(i for i in primes if prime_trunc(i))


if __name__ == "__main__":
    print("Math037")
    print("answer() =", answer(), "\n")
