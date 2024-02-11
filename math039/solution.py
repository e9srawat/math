"""Integer Right Triangles"""


def perimeter_counter(pmeter):
    """returns the number of solutions for pmeter"""
    count = 0
    for a in range(1, pmeter // 2):
        for b in range(a, (pmeter - a) // 2):
            c = pmeter - a - b
            if a**2 + b**2 == c**2:
                count += 1
    return count


def answer():
    """answer function"""
    pmeter_sols = 0
    max_pmeter = 0
    for i in range(1, 1001):
        if perimeter_counter(i) > pmeter_sols:
            pmeter_sols = perimeter_counter(i)
            max_pmeter = i
    return max_pmeter


if __name__ == "__main__":
    print("Math039")
    print("answer() =", answer(), "\n")
