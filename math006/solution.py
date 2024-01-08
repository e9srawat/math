"""Day 006"""


def solver(start, end):
    """Returns the difference between the sum and squares of sum between range start and end"""
    sum1 = (start - 1) * ((start - 1) + 1) // 2
    sum2 = end * (end + 1) // 2
    sumf = sum2 - sum1

    sqsum1 = (start - 1) * ((start - 1) + 1) * ((2 * (start - 1)) + 1) // 6
    sqsum2 = end * (end + 1) * (2 * end + 1) // 6
    sqsum = sqsum2 - sqsum1

    result = sumf**2 - sqsum

    return result


def answer():
    """Returns the difference between the sum and squares of sum between range 1 and 100"""
    return solver(1, 100)

if __name__ == "__main__": 
    print("Math006") 
    print("answer() =",answer())
    print("solver(200, 500) =",solver(200, 500))
    print("\n")
