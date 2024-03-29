"""
Powerful Digit Sum
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
    value = 0
    for i in range(1, 101):
        for j in range(1, 101):
            result = powerf(i, j)
            x = [int(a) for a in str(result)]
            if sum(x) > value:
                value = sum(x)
    return value


if __name__ == "__main__":
    print("Math056")
    print("answer() =", answer(), "\n")
