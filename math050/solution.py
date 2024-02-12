"""Consecutive Prime Sum"""


def is_prime(num):
    """finds if num is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer():
    """answer function"""
    primes = [i for i in range(1, 1000001) if is_prime(i)]
    prime_list = [i for i in primes if i > 1000]
    for i in primes:
        addr = [i]
        for j in primes[primes.index(i) + 1 :]:
            addr.append(j)
            if sum(addr) in prime_list:
                return sum(addr)
    return None


if __name__ == "__main__":
    print("Math050")
    print("answer() =", answer(), "\n")
