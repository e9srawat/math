"""Coded Triangle Numbers"""


def triangle_gen(num):
    """genrates num triangle numbers"""
    lst = [int((1 / 2 * i) * (i + 1)) for i in range(1, num + 1)]
    return lst


def answer():
    """answer function"""
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphadict = {alphabets[i]: i + 1 for i in range(0, len(alphabets))}
    with open("words.txt", "r", encoding="UTF-8") as file:
        reader = file.read()
        data = [char for char in list(reader) if char != '"']
        data = ("".join(data)).split(",")
    biggest = max(len(i) for i in data)
    triangles = triangle_gen(biggest * 26)
    lst = []
    for i in data:
        value = 0
        for j in i:
            value += alphadict[j]
        if value in triangles:
            lst.append(i)
    return len(lst)


if __name__ == "__main__":
    print("Math042")
    print("answer() =", answer(), "\n")
