# def powerf(num, power):
#     """
#     finds power of num
#     """
#     prod = str(num)
#     for _ in range(power - 1):
#         res = []
#         carry = 0

#         for j in prod[::-1]:
#             if carry:
#                 result = str(num * int(j) + int(carry))
#             else:
#                 result = str(num * int(j))
#             res.append(result[-1])
#             carry = result[:-1]
#         res.append(carry)
#         res = res[::-1]
#         prod = "".join(res)
#     return int(prod)

def powerf(num, power):
    """
    finds power of num
    """
    if power == 0:
        return 1
    elif power % 2 == 0:
        half_power = power // 2
        temp = powerf(num, half_power)
        return temp * temp
    else:
        return num * powerf(num, power - 1)

def answer():
    """
    answer function
    """
    n=1000
    lst = []
    for i in range(1,10):
        print(i)
        for j in range(1,n):
            l = len(str(powerf(i,j)))
            if l==j:
                lst.append(i)
    print(len(lst)) 
    
