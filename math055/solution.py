def is_palindrome(num):
    """checks if num is palindrome or not"""
    if list(str(num)) == list(str(num))[::-1]:
        return True
    return False

def answer():
    """
    answer function
    """
    lnums=0
    for i in range(1,10000):
        iterations = 0
        num=i
        lychrel=False
        while iterations<=50:
            sum = num + int(str(num)[::-1])
            num = sum
            if is_palindrome(sum):
                break
            if iterations==50:
                lychrel=True
            iterations+=1
        if lychrel:
            lnums+=1
    return lnums

print(answer())
    