"""
Non-Abundant Sums
"""

import math


def factors(num):
    """Returns sum of all factors (except num) of num"""
    factor = [i for i in range(1, round(math.sqrt(num) + 1)) if num % i == 0]
    mirror = [int(num / i) for i in range(1, round(math.sqrt(num) + 1)) if num % i == 0]
    if factor:
        allf = set(factor + mirror)
        allf.remove(num)
        return sum(allf)
    return None


def answer():
    """returns the sum of all the positive integers
    which cannot be written as the sum of two abundant numbers"""
    abundn = [i for i in range(28124) if factors(i) and factors(i) > i]
    abundn_sum = [
        i + abundn[j] for i in abundn for j in range(abundn.index(i), len(abundn))
    ]
    return len(abundn_sum)


def solver():
    """returns the sum of all the positive
    integers which cannot be written as the sum of two abundant numbers"""
    return -1


if __name__ == "__main__":
    print("Math023")
    print("answer() =", answer(), "\n")
