"""Day004"""


def solver(n, p=None, q=None):
    """returns largest palindrome form the product of two n digit numbers between p and q"""
    if not p and not q:
        p = int("1" + "0" * (n - 1))
        q = int("1" + "0" * (n))
    elif not p:
        p = int("1" + "0" * (n - 1))
    elif not q:
        q = p
        p = int("1" + "0" * (n - 1))
    palindrome = 0
    for i in reversed(range(p, q)):
        for j in reversed(range(p, i + 1)):
            product = i * j
            if str(product) == "".join(reversed(str(product))) and product > palindrome:
                palindrome = product
    return palindrome


def answer():
    """returns largest palindrome form the product of two 3 digit numbers between 100 and 999"""
    palindrome = solver(3, 100, 999)
    return palindrome


if __name__ == "__main__":
    print("Math004")
    print("answer() =", answer())
    print("solver(4, 2000, 5000) =", solver(4, 2000, 5000))
    print("\n")
