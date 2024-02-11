"""Consecutive Prime Sum"""


def is_prime(num):
    """finds if num is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_til_n(num):
    """returns prime numbers till num"""
    dicn = {i: "not prime" for i in range(1, num + 1)}
    for i in dicn:
        if is_prime(i):
            dicn[i] = "prime"
    lst = [i for i in dicn if dicn[i] == "prime"]
    return lst


def answer():
    """answer function"""
    primes = prime_til_n(1000000)
    prime_list = [i for i in primes if i > 1000]
    print(prime_list)
    k = 997651
    for i in primes:
        addr = [i]
        for j in primes[primes.index(i) + 1 :]:
            addr.append(j)
            if sum(addr) == k:
                return addr
            if sum(addr) > k:
                break
    return None


if __name__ == "__main__":
    print("Math050")
    print("answer() =", answer(), "\n")
