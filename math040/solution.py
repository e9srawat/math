"""Champernowne's Constant"""


def answer():
    """answer function"""
    string = ""
    for i in range(1, 1000001):
        string += str(i)
    return (
        int(string[0])
        * int(string[9])
        * int(string[99])
        * int(string[999])
        * int(string[9999])
        * int(string[99999])
        * int(string[999999])
    )


if __name__ == "__main__":
    print("Math040")
    print("answer() =", answer(), "\n")
