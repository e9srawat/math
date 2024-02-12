"""
Circular Primes
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


def rotato(num):
    """rotates the number"""
    return [str(num)[j:] + str(num)[:j] for j in range(1, len(str(num)))]


def answer():
    """returns circular primes are there below one million"""
    prime = primes(1000000)
    lest = []
    for i in prime:
        lst = all(is_prime(int(j)) for j in rotato(i))
        if lst:
            lest.append(i)
    return len(lest)


if __name__ == "__main__":
    print("Math035")
    print("answer() =", answer(), "\n")
