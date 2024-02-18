"""
Permuted Multiples
"""


def answer():
    """
    answer function
    """
    for i in range(1, 1000000):
        num1 = sorted(str(i * 2))
        num2 = sorted(str(i * 3))
        num3 = sorted(str(i * 4))
        num4 = sorted(str(i * 5))
        num5 = sorted(str(i * 6))
        if num1 == num2 == num3 == num4 == num5:
            return i
    return None


if __name__ == "__main__":
    print("Math052")
    print("answer() =", answer(), "\n")
