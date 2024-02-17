"""Triangular, Pentagonal, and Hexagonal"""


def pentagon(num):
    """generates num pentagon numbers from 10000 to num"""
    lst = [int(i * (3 * i - 1) / 2) for i in range(10000, num + 1)]
    return lst


def hexagon(num):
    """generates hexagon numbers from 10000 to num"""
    lst = [int(i * (2 * i - 1)) for i in range(10000, num + 1)]
    return lst


def answer():
    """answer function"""
    # triangles = triangle(100000)
    pentagons = pentagon(100000)
    hexagons = hexagon(100000)
    lst = [i for i in hexagons if i in pentagons]
    return lst


if __name__ == "__main__":
    print("Math045")
    print("answer() =", answer(), "\n")
