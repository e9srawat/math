"""Math 015"""


def answer():
    """
    Returns the number of possible routes from top left
    to bottom right corner in a 20x20 grid
    """
    return solver(20, 20)


def solver(n, m):
    """
    Returns the number of possible routes from top left
    to bottom right corner in a nxm grid
    """
    lst = [[1 if i == 0 else 0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m):
        s = 1
        for j in range(1, n + 1):
            s = s + lst[i][j]
            lst[i + 1][j] = s
    return lst[-1][-1]


if __name__ == "__main__":
    print("Math015")
    print("answer() =", answer())
    print("solver(30,30) =", solver(30, 30))
    print("\n")
