"""Prime Permutations"""


def is_prime(num):
    """returns num prime numbers"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer():
    """answer function"""
    for i in range(1000, 10000):
        num1 = i + 3330
        num2 = i + 6660
        if is_prime(i) and is_prime(num1) and is_prime(num2):
            if sorted(str(num1)) == sorted(str(num2)) == sorted(str(i)) and i != 1487:
                lst = [str(i), str(num1), str(num2)]
    return "".join(lst)


if __name__ == "__main__":
    print("Math049")
    print("answer() =", answer(), "\n")
