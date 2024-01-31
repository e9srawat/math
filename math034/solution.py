"""
Digit Factorials
"""


def fact(num):
    """finds factorial of num"""
    fac_sum = 1
    for i in range(1, num + 1):
        fac_sum *= i
    return fac_sum


def answer():
    """returns sum of all numbers which are equal to the sum of the factorial of their digits"""
    lst = []
    for i in range(10, 1000000):
        fact_sum = 0
        for j in str(i):
            fact_sum += fact(int(j))
        if fact_sum == i:
            lst.append(i)
    return sum(lst)


if __name__ == "__main__":
    print("Math034")
    print("answer() =", answer(), "\n")
