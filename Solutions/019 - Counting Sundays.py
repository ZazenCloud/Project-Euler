def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month != 2:
        return 31
    else:
        return 29 if is_leap_year(year) else 28


sundays = 0
day = 0
month = 1
year = 1901

while year <= 2000:
    while month <= 12:
        if day == 0:
            sundays += 1
        day = (day + days_in_month(month, year)) % 7
        month += 1
    month = 1
    year += 1

print(sundays)
