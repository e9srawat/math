"""Sub-String Divisibility"""


def get_combinations(digits, current="", combinations=None):
    """returns all possible combinations of a string of elements"""
    if combinations is None:
        combinations = []

    if not digits:
        combinations.append(current)
        return combinations

    for i in range(len(digits)):
        remaining_digits = digits[:i] + digits[i + 1 :]
        combinations = get_combinations(
            remaining_digits, current + digits[i], combinations
        )

    return combinations


def check(num):
    """check if num satisfies the condition"""
    dicn = {
        num[1:4]: 2,
        num[2:5]: 3,
        num[3:6]: 5,
        num[4:7]: 7,
        num[5:8]: 11,
        num[6:9]: 13,
        num[7:10]: 17,
    }
    for i in dicn:
        if int(i) % dicn[i] != 0:
            return False
    return True


def answer():
    """answer function"""
    lst = []
    numbers = get_combinations("1234567890")
    for i in numbers:
        if check(i):
            lst.append(int(i))
    return sum(lst)


if __name__ == "__main__":
    print("Math043")
    print("answer() =", answer(), "\n")
