""" 
Totient Maximum
"""


def is_prime(num):
    """finds if num is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes(n):
    """returns a list of primes till n"""
    return [i for i in range(2, n + 1) if is_prime(i)]


def answer():
    """
    answer function
    """
    totient = 1
    prime_nums = primes(1000000)
    for i in prime_nums:
        if totient * i > 1000000:
            break
        totient *= i
    return totient


if __name__ == "__main__":
    print("Math069")
    print("answer() =", answer(), "\n")
