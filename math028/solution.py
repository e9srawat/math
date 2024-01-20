"""
Number Spiral Diagonals
"""


def is_eve_odd(n):
    """
    finds if n is even or odd
    """
    if n % 2 == 0:
        return "even"
    return "odd"


def answer():
    """
    returns the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    """
    return solver(1001)


def solver(n):
    """
    returns the sum of the numbers on the diagonals in a n by n spiral
    """
    if is_eve_odd(n) == "even":
        lst = [0]
        addr = 1
        start = 1
    else:
        lst = [1]
        addr = 2
        start = 3
    count = 0
    while lst[-1] != n * n:
        lst.append(start)
        count += 1
        if count == 4:
            addr += 2
            count = 0
        start += addr
    return sum(lst)


if __name__ == "__main__":
    print("Math028")
    print("answer() =", answer())
    print("solver('1000') =", solver(1000))
    print("\n")
