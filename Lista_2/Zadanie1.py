from datetime import datetime


def compute_Easter_date(year: int = 1990):
    """
    Function calculates the date of Easter Sunday in a given year.
    Based on the Jean Meeus algorithm.
    :param year: Year that we want to check the date of Easter Sunday.
    :return: Date (day, month and year) of Easter Sunday.
    """
    if year < 0:
        raise ValueError("Year cannot be a negative number.")
    elif type(year) is not int:
        raise ValueError("Year type must be int.")
    else:
        a = year % 19
        b = int(year / 100)
        c = year % 100
        d = int(b / 4)
        e = b % 4
        f = int((b + 8) / 25)
        g = int((b - f + 1) / 3)
        h = (19 * a + b - d - g + 15) % 30
        i = int(c / 4)
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = int((a + 11 * h + 22 * l) / 451)
        p = (h + l - 7 * m + 114) % 31
        day = p + 1
        month = int((h + l - 7 * m + 114) / 31)
        date = datetime(year, month, day)

    return date.strftime("%d %B %Y")


print(compute_Easter_date(2012))
