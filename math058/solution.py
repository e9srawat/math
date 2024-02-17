"""
Spiral Primes
"""


def is_prime(n):
    """
    check for prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True


def asnswer():
    """
    answer function
    """
    addr = 0
    loop = 0
    lst = [1]
    prev = [1, 1, 1, 1]
    primes = []
    while True:
        lst.append(2 * (1 + addr) + prev[0])
        lst.append(2 * (2 + addr) + prev[1])
        lst.append(2 * (3 + addr) + prev[2])
        lst.append(2 * (4 + addr) + prev[3])
        prev = [lst[-4:][0], lst[-3:][0], lst[-2:][0], lst[-1]]
        for i in prev:
            if is_prime(i):
                primes.append(i)
        primen = len(primes)
        total = len(lst)
        addr += 4
        loop += 1
        if int((primen / total) * 100) < 10:
            return loop * 2 + 1
