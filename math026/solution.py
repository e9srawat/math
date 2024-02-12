"""
Reciprocal Cycles
"""


def get_den(n):
    """returns reciprocating digits of 1/n"""
    lst = []
    num = 1
    nums = set()
    while True:
        div = num // n
        num = num % n
        lst.append(div)
        if num == 0 or (num in nums):
            break
        nums.add(num)
        num = num * 10
    return lst[1:]


def answer():
    """returns the value of d<1000 for which 1/d contains
    the longest recurring cycle in its decimal fraction part"""
    return solver(1000, [])


def solver(n, lst: []):
    """returns the value of d/n for which 1/n contains all the
    digits in the provided list in the recurring cycle in its decimal fraction part."""
    mx = 0
    mx_index = 0
    for i in range(2, n + 1):
        val = len(get_den(i))
        if lst:
            if all(j in get_den(i) for j in lst):
                return i
        if val > mx:
            mx = val
            mx_index = i
    return mx_index


if __name__ == "__main__":
    print("Math026")
    print("answer() =", answer())
    print("solver(1000,[1, 4, 2, 8, 5, 7]) =", solver(1000, [1, 4, 2, 8, 5, 7]))
    print("\n")
