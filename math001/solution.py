"""Day001"""


def solver(factors, start, end):
    """sum of all the multiples of factors, multiples are between the start and end, inclusive"""
    multiples = []
    for i in range(start, end):
        for j in factors:
            if i % j == 0 and i not in multiples:
                multiples.append(i)
    return sum(multiples)


def answer():
    """The sum of all the multiples of 3 or 5 below 1000."""
    return solver([3, 5], 1, 1000)

if __name__ == "__main__": 
    print("Math001") 
    print("answer() =",answer())
    print("solver([3,4, 5], 1, 1000) =",solver([3,4, 5], 1, 1000))
    print("\n")