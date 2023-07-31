def is_leap_year(year):
    """Checks if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    """Counts the number of days in a month."""
    if month in [4, 6, 9, 11]:
        return 30
    elif month != 2:
        return 31
    else:
        return 29 if is_leap_year(year) else 28


sundays = 0
day = 0  # 0 for Sunday, 1 for Monday, etc.
month = 1
year = 1901

# Loops through the years from 1901 to 2000
while year <= 2000:
    # Loops through the months from January to December
    while month <= 12:
        # Checks if the first day of the month is a Sunday
        if day == 0:
            sundays += 1
        # Calculates the day of the week of the first day of the next month
        day = (day + days_in_month(month, year)) % 7
        month += 1
    # Resets the month to January
    month = 1
    year += 1

print(sundays)
