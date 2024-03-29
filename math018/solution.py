"""Math 018"""

TRI = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

TRI2 = """58
95 64
17 54 82
18 35 87 10
20 04 82 47 65
19 01 93 75 56 34
88 89 77 99 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 90 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 04 33 28 77 73 17 78 39 68 17 57
91 71 34 38 17 14 91 43 58 12 27 29 48
63 66 04 77 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 98 53 60 04 23"""


def answer():
    """returns maximum total from top to bottom
    of the triangle of height 15"""

    return solver(TRI)


def solver(n):
    """returns maximum total from top to bottom
    of the triangle of variable height"""
    n = n.split("\n")
    print(n)

    # intn = [[int(j) for j in i.split(" ")] for i in n]

    # for i in reversed(range(len(intn) - 1)):
    #     for j in range(len(intn[i])):
    #         intn[i][j] += max(intn[i + 1][j], intn[i + 1][j + 1])
    # return intn[0][0]


if __name__ == "__main__":
    print("Math018")
    print("answer() =", answer())
    print("solver(tri2) =", solver(TRI2))
    print("\n")
