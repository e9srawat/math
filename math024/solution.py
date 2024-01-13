"""
Lexicographic Permutations
"""
import math


def factorial(num):
    """returns factorial of num"""
    return math.prod(list(range(1, num + 1)))


def answer():
    """returns the 1000000th lexicographic permutation of 0123456789"""
    return solver("0123456789", 1000000)


def solver(p, n):
    """returns the nth lexicographic permutation of a string"""
    lst = list(p)
    n -= 1
    lex = []
    for i in reversed(range(len(p))):
        pos = n // factorial(i)
        n %= factorial(i)
        lex.append(lst.pop(pos))
    return "".join(lex)


if __name__ == "__main__":
    print("Math024")
    print("answer() =", answer())
    print(
        "solver('123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',20000') =",
        solver("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", 20000),
    )
    print("\n")
