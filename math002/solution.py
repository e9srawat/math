"""Day 002"""


def solver(start, end, even=False, odd=False):
    """Day 002"""
    if start > end:
        return "none"

    fibonacci = [1, 2]
    while fibonacci[-1] < end:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    fibo = [i for i in fibonacci if i >= start]

    if even and odd:
        return sum(fibo)

    if even:
        return sum(i for i in fibo if i % 2 == 0)

    if odd:
        return sum(i for i in fibo if i % 2 != 0)

    return 0


def answer():
    """sum of Fibonacci sequence whose values smaller than 4000000"""
    return solver(start=1, end=4000000, even=True, odd=False)

if __name__ == "__main__": 
    print("Math002") 
    print("answer() =",answer())
    print("solver(start=20000, end=4000000, even=True, odd=False) =",solver(start=20000, end=4000000, even=True, odd=False))
    print("\n")
