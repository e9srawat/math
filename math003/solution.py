"""Day 003"""

import math


def is_prime(num):
    """Returns true if num is prime"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solver(value):
    """Returns the largest prime factor for value"""
    if value < 2:
        return "Enter a value greater than 1"
    sqrt_num = round(math.sqrt(value))
    factors = [i for i in range(1, sqrt_num + 1) if value % i == 0]
    mirrors = [int(value / i) for i in range(1, sqrt_num + 1) if value % i == 0]
    prime = [i for i in factors + mirrors if is_prime(i)]
    return max(prime)


def answer():
    """Returns the largest prime favtor for 600851475143"""
    return solver(600851475143)


if __name__ == "__main__":
    print("Math003")
    print("answer() =", answer())
    print("solver(2345613567) =", solver(2345613567))
    print("\n")
