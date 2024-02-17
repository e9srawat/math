"""
Square Root Convergents
"""


def fraction_f(num, frac):
    """
    returns sum in fraction format of a number and a fraction
    """
    frac_split = frac.split("/")
    nume = int(num) * int(frac_split[1])
    if len(frac_split) == 3:
        nume = nume + int(frac_split[2])
    else:
        nume = nume + int(frac_split[0])
    return f"{nume}/{frac_split[1]}"


def answer():
    """
    answer function
    """
    den = 2
    lst = []
    for _ in range(1000):
        fraction = fraction_f("1", f"1/{den}")
        if len(fraction.split("/")[0]) > len(fraction.split("/")[1]):
            lst.append(fraction)
        den = fraction_f("2", f"1/{den}")
    return len(lst)
