"""Pandigital Multiples"""


def is_pandigital(number):
    """finds if the given number is pandigital or not"""
    digits = [str(i) for i in range(1, 10)]
    if sorted(str(number)) == digits:
        return True
    return False


def answer():
    """answer function"""
    max_pan = 0
    for i in range(1, 10000):
        product = ""
        n = 1
        while len(product) < 9:
            product += str(i * n)
            n += 1
        if is_pandigital(int(product)):
            max_pan = max(max_pan, int(product))
    return max_pan


if __name__ == "__main__":
    print("Math038")
    print("answer() =", answer(), "\n")
