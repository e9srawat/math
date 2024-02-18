""" 
Powerful Digit Counts
"""


def powerf(num, power):
    """
    finds power of num
    """
    if power == 0:
        return 1
    if power % 2 == 0:
        half_power = power // 2
        temp = powerf(num, half_power)
        return temp * temp
    return num * powerf(num, power - 1)


def answer():
    """
    answer function
    """
    lst = []
    for i in range(1, 10):
        for j in range(1, 1000):
            l = len(str(powerf(i, j)))
            if l == j:
                lst.append(i)
    return len(lst)


if __name__ == "__main__":
    print("Math063")
    print("answer() =", answer(), "\n")
