"""
return dictionary of list of tuples
"""
import math


def solver(p: int, q: int = None):
    """
    return dictionary of list of tuples
    """
    res = {}
    if not q:
        q = p
        p = 1
    for n in range(p, q + 1):
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                c = a**2 + b**2
                if a + b + math.sqrt(c) == n:
                    if n not in res:
                        res[n] = []
                    res[n].append((a, b, int(math.sqrt(c))))
    return res


def answer():
    """
    returns triplet for sum = 1000
    """
    result = solver(1000, 1000)
    return result

if __name__ == "__main__": 
    print("Math009") 
    print("answer() =",answer())
    print("solver(10000,10000) =",solver(10000,10000))
    print("\n")

