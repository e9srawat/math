"""Double-base Palindromes"""


def dec_to_bin(num):
    """converts decimal number to binary"""
    lst = []
    while num != 0:
        lsb = num % 2
        lst.append(str(lsb))
        num = int(num / 2)
    return int("".join(lst[::-1]))


def is_palindrome(num):
    """checks if num is palindrome or not"""
    if list(str(num)) == list(str(num))[::-1]:
        return True
    return False


def answer():
    """answer function"""
    return sum(
        i
        for i in range(1, 1000000)
        if is_palindrome(i) and is_palindrome(dec_to_bin(i))
    )


if __name__ == "__main__":
    print("Math036")
    print("answer() =", answer(), "\n")
