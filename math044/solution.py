"""Pentagon Numbers"""


def penta_gen(num):
    """generates pentagonal numbers till num"""
    penta = []
    starter = 1
    while len(penta) != num:
        penta.append(int(starter * (3 * starter - 1) / 2))
        starter += 1
    return penta


def answer():
    """answer function"""
    pentas = penta_gen(10000)
    visited = []
    for i in pentas:
        for j in visited:
            pentas_sum = i + j
            pentas_diff = i - j
            if pentas_sum in pentas and pentas_diff in pentas:
                return (i, j)
        visited.append(i)
    return None


if __name__ == "__main__":
    print("Math044")
    print("answer() =", answer(), "\n")
