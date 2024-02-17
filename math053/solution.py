import math

def factorial(num):
    """
    returns factorial of num
    """
    return math.prod(list(range(1, num + 1)))


def combos(n,r):
    """
    returns number of combinations
    """
    return factorial(n)//(factorial(r)*factorial(n-r))

def answer():
    """
    answer function
    """
    counter=0
    for n in range(1,101):
        for r in range(1,n):
            if combos(n,r)>1000000:
                counter+=1
    return counter
