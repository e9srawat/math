"""Coin Sums"""


def answer():
    """How many different ways can 2 be made using any number of coins?"""
    return solver(200)


def solver(n):
    """different number of ways to make any amount (n)?"""
    coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
    combos = [1] + [0] * n
    for i in coin_list:
        for j in range(len(combos) - i):
            combos[j + i] += combos[j]
    return str(combos[-1])


if __name__ == "__main__":
    print("Math031")
    print("answer() =", answer())
    print("solver(100) =", solver(100))
    print("\n")
