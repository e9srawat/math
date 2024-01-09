"""
Name Scores
"""


def answer():
    """returns total of all the name scores in the file"""
    return solver("math022/0022_names.txt")


def solver(names: str):
    """
    names is the name of the file with all the names for processing
    """
    alpha = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    with open(names, "r",encoding="utf-8") as file1:
        reader = file1.read()
    lst = sorted(reader.split(","))
    result = 0
    for i in lst:
        addr = 0
        for j in i:
            if j in alpha:
                addr += alpha[j]
        pos = lst.index(i) + 1
        score = pos * addr
        result += score
    return result


if __name__ == "__main__":
    print("Math021")
    print("answer() =", answer())
    print("solver('math022/names.txt') =", solver("math022/names.txt"))
    print("\n")
