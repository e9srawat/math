"""Distinct Primes Factors"""


def prime_factors(n):
    """finds prime factors of n"""
    factors = set()
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors


def answer():
    """answer function"""
    for i in range(130000, 200000):
        fact1 = prime_factors(i)
        fact2 = prime_factors(i + 1)
        fact3 = prime_factors(i + 2)
        fact4 = prime_factors(i + 3)

        if len(fact1) == len(fact2) == len(fact3) == len(fact4) == 4:
            return i
    return None


if __name__ == "__main__":
    print("Math047")
    print("answer() =", answer(), "\n")
