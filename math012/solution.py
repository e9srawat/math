"""
Math 012
"""
import math


def answer():
    """
    returns the first triangle number to have over five hundred divisors
    """

    return solver(500)


def f_factors(n):
    """Returns factors of n"""
    lst = [i for i in range(1, round(math.sqrt(n) + 1)) if n % i == 0]
    return lst


def solver(n):
    """returns the first triangle number to have over n divisors."""
    tri_num = 0
    count = 1
    while True:
        tri_num += count
        count += 1
        factors = f_factors(tri_num)
        if len(factors) >= n / 2:
            break
    return tri_num

if __name__ == "__main__":
    print("Math012") 
    print("answer() =",answer())
    print("solver(700) =",solver(700))
    print('\n')
