"""Triangular, Pentagonal, and Hexagonal"""


def pentagon(num):
    """generates num pentagon numbers"""
    lst = [int(i * (3 * i - 1) / 2) for i in range(10000, num + 1)]
    return lst


def hexagon(num):
    """generates num hexagon numbers"""
    lst = [int(i * (2 * i - 1)) for i in range(10000, num + 1)]
    return lst


def answer():
    """answer function"""
    # triangles = triangle(100000)
    pentagons = pentagon(100000)
    hexagons = hexagon(100000)
    lst = []
    for i in hexagons:
        print(i)
        if i in pentagons:
            lst.append(i)
    return lst


if __name__ == "__main__":
    print("Math045")
    print("answer() =", answer(), "\n")
