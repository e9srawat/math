"""
1000-digit Fibonacci
"""


def adder(num1, num2):
    """Adds two numbers"""
    smol = str(min(num1, num2))[::-1]
    big = str(max(num1, num2))[::-1]
    while len(smol) != len(big):
        smol += "0"
    carry = 0
    lst = []
    for i in range(len(str(smol))):
        sume = int(smol[i]) + int(big[i]) + int(carry)
        lst.append(str(sume)[-1])
        if str(sume)[:-1]:
            carry = str(sume)[:-1]
        else:
            carry = 0
    if carry:
        lst.append(carry)
    return int("".join(lst[::-1]))


def answer():
    """returns the index of the first term in the Fibonacci sequence to contain 1000 digits"""
    return solver(1000)


def solver(n):
    """returns the index of the first term in the Fibonacci sequence to contain n digits"""
    lst = [1, 1]
    while len(str(lst[-1])) < n:
        lst.append(adder(lst[-2], lst[-1]))
    return lst.index(lst[-1])


if __name__ == "__main__":
    print("Math025")
    print("answer() =", answer())
    print("solver('500') =", solver(500))
    print("\n")
