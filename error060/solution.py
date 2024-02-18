
# Import time module
import time
 
# record start time
start = time.time()
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

def check_prop(a,b):
    return is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a)))

def answer():
    lst = [3,7,109,673]
    primes_list = primes(30000)
    for i in primes_list:
        print(i)
        flag = True
        for j in lst:
            if not check_prop(i,j):
                flag = False
                break
        if flag:
            print(i) 
            
            
answer()
