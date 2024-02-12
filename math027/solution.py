"""
Quadratic Primes
"""

import math


def isprime(n):
    """Finds if a number is prime or not"""
    n = abs(n)
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# n2+an+b


def primer(a, b):
    """
    finds if n2+an+b gives primes for n starting with 0
    if it does, returns the number of prime numbers it can
    """
    n = 0
    eqn = n**2 + a * n + b
    lst = []
    while isprime(eqn):
        lst.append(eqn)
        n += 1
        eqn = n**2 + a * n + b

    return len(lst)


def answer():
    """
    returns product of the coefficients a and b for the quadratic expression
    that produces the maximum number of primes for consecutive values of n
    """
    a, b = 1, 1
    biggest = 0
    for i in range(-1000, 1001):
        for j in range(-999, 1000):
            if primer(i, j) > biggest:
                biggest = primer(i, j)
                a = j
                b = i
    return a * b


if __name__ == "__main__":
    print("Math027")
    print("answer() =", answer())
    print("\n")
