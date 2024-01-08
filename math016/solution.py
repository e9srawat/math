"""MATH 016"""


def answer():
    """
    Returns sum of digits of 2^1000
    """
    return solver(1000)


def solver(n):
    """
    Returns sum of digits of 2^n
    """
    starter = "1"
    for i in range(n):
        carry = None
        product = "0"
        fprod = []
        for j in reversed(range(len(str(starter)))):
            if carry:
                if j == 0:
                    product = str((int(starter[j]) * 2) + int(carry))
                    fprod.append(product)
                    break
                product = str((int(starter[j]) * 2) + int(carry))
            else:
                if j == 0:
                    product = str((int(starter[j]) * 2))
                    fprod.append(product)
                    break
                product = str(int(starter[j]) * 2)
            carry = product[:-1]
            product = product[-1]
            fprod.append(product)
        starter = "".join(reversed(fprod))

    return sum(int(i) for i in starter)


if __name__ == "__main__":
    print("Math016")
    print("answer() =", answer())
    print("solver(1000) =", solver(10000))
    print("\n")
