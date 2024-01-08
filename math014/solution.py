"""
math 014
"""


def answer():
    """
    returns the number under 1 million,
    which produces the longest collatz sequence chain
    """
    return solver(1000000)


def odd_eve(num):
    """
    returns if num is odd or even
    """
    if num % 2 == 0:
        return "even"
    return "odd"


def solver(p: int = None, q: int = None):
    """
    returns the number, which produces the longest collatz sequence chain
    between the given range
    """
    if not p and not q:
        return None
    if not q:
        q = p
        p = 2

    hash_t = {}
    size = 0
    for i in range(p, q + 1):
        lst = [i]
        n = i
        while True:
            if odd_eve(n) == "even":
                n = int((n / 2))
            elif odd_eve(n) == "odd":
                n = int((3 * n) + 1)
            if n in hash_t:
                lst = lst + hash_t[n]
                break
            lst.append(n)
            if n == 1:
                break
        if len(lst) > size:
            size = len(lst)
            biggest = i
        hash_t[i] = lst
    return biggest


if __name__ == "__main__":
    print("Math014")
    print("answer() =", answer())
    print("solver(1000) =", solver(1000))
    print("\n")
