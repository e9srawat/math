"""Day005"""


def gcd(a, b):
    """GCD of a, b"""
    mx = max(a, b)
    mn = min(a, b)
    while mn:
        temp = mx
        mx = mn
        mn = temp % mn
    return mx


def solver(p, q):
    """lcm from range p-q"""
    start = min(p, q)
    end = max(p, q)
    lcm = 1
    for i in range(start, end + 1):
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def answer():
    """lcm from range 1-20"""
    return solver(1, 20)

if __name__ == "__main__": 
    print("Math005") 
    print("answer() =",answer())
    print("solver(20, 50) =",solver(20, 50))
    print("\n")
