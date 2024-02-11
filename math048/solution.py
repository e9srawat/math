"""Self Powers"""


def self_power(num):
    """Finds num^num"""
    result = str(num)
    for _ in range(num - 1):
        carry = ""
        prod = []
        for j in result[::-1]:
            if carry:
                prod.append(str(num * int(j) + int(carry))[-1:])
                carry = str(num * int(j) + int(carry))[:-1]
            else:
                prod.append(str(num * int(j))[-1:])
                carry = str(num * int(j))[:-1]
        prod.append(carry)
        result = "".join(prod[::-1])
    return int(result)


def answer():
    """answer function"""
    lst = [self_power(i) for i in range(1, 1001)]
    return str(sum(lst))[-10:]


if __name__ == "__main__":
    print("Math048")
    print("answer() =", answer(), "\n")
