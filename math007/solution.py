"""finds nth prime number"""
import math


def is_prime(num):
    """checks if num is prime"""
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def solver(n: int):
    """finds nth prime number"""
    counter = 3
    prime = 5
    while True:
        prime += 1
        if prime % 2 != 0 and prime % 5 != 0:
            if is_prime(prime):
                counter += 1
        if counter == n:
            return prime


def answer():
    """finds 10001th prime number"""
    return solver(10001)

if __name__ == "__main__": 
    print("Math007") 
    print("answer() =",answer())
    print("solver(100001) =",solver(100001))
    print("\n")
