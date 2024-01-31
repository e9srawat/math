"""
Digit Cancelling Fractions
"""

import math


def gcd(a, b):
    """GCD of a, b"""
    mx = max(a, b)
    mn = min(a, b)
    while mn:
        temp = mx
        mx = mn
        mn = temp % mn
    return (int(a / mx), int(b / mx))


def common_cancel(num1, num2):
    """solves fractions the wrong way"""
    num1 = list(str(num1))
    num2 = list(str(num2))
    for i in num1:
        if i in num2:
            index1 = num1.index(i)
            index2 = num2.index(i)
            num1.remove(num1[index1])
            num2.remove(num2[index2])
            num1, num2 = "".join(num1), "".join(num2)
            return int(num1) / int(num2)
    return None


def answer():
    """answer function"""
    nums = []
    den = []
    for i in range(10, 100):
        for j in range(i + 1, 100):
            if str(i)[-1] != "0" and str(j)[-1] != "0" and i != j:
                if common_cancel(i, j) == i / j:
                    nums.append(gcd(i, j)[0])
                    den.append(gcd(i, j)[1])
    productn = math.prod(nums)
    productd = math.prod(den)

    return gcd(productn, productd)[1]


if __name__ == "__main__":
    print("Math033")
    print("answer() =", answer(), "\n")
