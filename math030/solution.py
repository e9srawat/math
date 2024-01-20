"""
Digit Fifth Powers
"""


def answer():
    """returns sum of all the numbers that can be written as the sum of
    fifth powers of their digits"""
    return solver(5)


def solver(n):
    """returns sum of all the numbers that can be written as the sum of
    nth powers of their digits"""
    small = int("1" + "0" * (n - 1))
    big = int("9" * n)
    return sum(i for i in range(small, big) if sum(int(j) ** n for j in str(i)) == i)


if __name__ == "__main__":
    print("Math030")
    print("answer() =", answer())
    print("solver(4) =", solver(4))
    print("\n")
