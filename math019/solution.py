"""Math 019"""
import datetime


def answer():
    """Returns the number of sundays from 1901-01-01 to 2000-12-31"""

    return solver(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31))


def num_days(year, month):
    """Returns number of days in the given month"""
    thirtyones = [1, 3, 5, 7, 8, 10, 12]
    thirtys = [4, 6, 9, 11]
    if month in thirtyones:
        return 31
    if month in thirtys:
        return 30
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        return 28
    return None


def solver(start: datetime.date, end: datetime.date):
    """Returns the number of sundays between the given dates"""
    year = 1900
    day = 1
    counter = 0
    month = 1
    sundate = day + 6
    while True:
        daynum = num_days(year, month)
        while sundate <= daynum:
            sundate += 7
        if sundate > daynum:
            sundate -= daynum
        month += 1
        if year >= start.year and sundate == 1:
            counter += 1
        if year == end.year and month == end.month:
            break
        if month > 12:
            year += 1
            month = 1

    return counter


if __name__ == "__main__":
    print("Math019")
    print("answer() =", answer())
    print(
        "solver((1903-1-1),(2000-12-31)) =",
        solver(datetime.date(1903, 1, 1), datetime.date(2000, 12, 31)),
    )
    print("\n")
