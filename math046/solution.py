"""Goldbach's Other Conjecture"""

import math


def primes_gen(n):
    """genrates n prime numbers"""
    num = 2
    prime = []
    while len(prime) < n:
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            prime.append(num)
        num += 1

    return prime


def composites_gen(n):
    """genrates n composite numbers"""
    num = 3
    composite = []
    while len(composite) < n:
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if not is_prime:
            composite.append(num)
        num += 2
    return composite


def answer():
    """answer function"""
    prime_nums = primes_gen(10000)
    composites_nums = composites_gen(10000)
    flag = True
    for i in composites_nums:
        flag = True
        for j in prime_nums:
            if j < i:
                x = (i - j) // 2
                if math.sqrt(x) == int(math.sqrt(x)):
                    flag = False
                    break
        if flag is True:
            return i
    return None


if __name__ == "__main__":
    print("Math046")
    print("answer() =", answer(), "\n")
