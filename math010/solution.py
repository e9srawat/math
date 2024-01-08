"""solver function"""
import math


def is_prime(n):
    """check for prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def solver(p: int, q: int = None):
    """returns sum of primes between range"""
    if not q:
        q = p
        p = 1
    if q < p:
        return None

    primes = [i for i in range(p, q + 1) if is_prime(i)]
    return sum(primes)


def answer():
    """Returns sum of prime numbers till 2000000"""
    return solver(2000000)

if __name__ == "__main__": 
    print("Math010") 
    print("answer() =",answer())
    print("solver(200000) =",solver(200000))
    print("\n")
