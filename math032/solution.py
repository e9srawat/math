"""Pandigital Products"""


def answer():
    """sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital."""

    d = [str(i) for i in range(1, 10)]
    my_set = set()

    for i in range(10, 100):
        for j in range(100, 1000):
            s = ""
            s = s + str(i)
            s = s + str(j)
            s = s + str(i * j)
            if sorted(s) == d:
                my_set.add(i * j)

    for i in range(10):
        for j in range(1000, 10000):
            s = ""
            s = s + str(i)
            s = s + str(j)
            s = s + str(i * j)
            if sorted(s) == d:
                my_set.add(i * j)

    return sum(my_set)


if __name__ == "__main__":
    print("Math032")
    print("answer() =", answer(), "\n")