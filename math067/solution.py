"""
Maximum Path Sum II
"""
def solver(n):
    """returns maximum total from top to bottom
    of the triangle of variable height"""
    n = n.split("\n")[:-1]

    intn = [[int(j) for j in i.split(" ")] for i in n]

    for i in reversed(range(len(intn) - 1)):
        for j in range(len(intn[i])):
            intn[i][j] += max(intn[i + 1][j], intn[i + 1][j + 1])
    return intn[0][0]

def answer():
    """
    answer function
    """
    with open('triangle.txt', "r", encoding="utf-8") as f:
        data = f.read()
    return solver(data)

print(answer())