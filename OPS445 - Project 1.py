#!/usr/bin/env python3

# ----------------------------------------
# OPS445 Assignment 1 – Date Calculator
# Author: Mehran Ebrahimi
# Description: Calculates leap years, next/previous day, date validation,
#              and date offset calculations.
# ----------------------------------------

# Check if a year is a leap year
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Leap year (divisible by 400)
            else:
                return False  # Not leap year (divisible by 100 but not 400)
        else:
            return True  # Leap year (divisible by 4 but not 100)
    else:
        return False  # Not leap year

# Get the maximum days in a given month, considering leap years
def mon_max(month, year):
    if month == 2:
        if leap_year(year):
            return 29  # February in leap year
        else:
            return 28  # February in normal year
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31  # Months with 31 days
    elif month in [4, 6, 9, 11]:
        return 30  # Months with 30 days

# Return the date of the next day
def after(date):
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1
    if day > mon_max(mon, year):
        day = 1
        mon += 1
        if mon > 12:
            mon = 1
            year += 1
    return f"{day:02}/{mon:02}/{year}"

# Return the date of the previous day
def before(date):
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1
    if day == 0:
        mon -= 1
        if mon == 0:
            mon = 12
            year -= 1
        day = mon_max(mon, year)
    return f"{day:02}/{mon:02}/{year}"

# Check if a given date string is valid
def valid_date(date):
    try:
        day, mon, year = (int(x) for x in date.split('/'))
        if year < 1583:
            return False  # Before Gregorian calendar
        if not (1 <= mon <= 12):
            return False  # Invalid month
        if not (1 <= day <= mon_max(mon, year)):
            return False  # Invalid day for the given month/year
        return True
    except:
        return False  # Error parsing date format

# Get the day of the week for a given date (Sun, Mon, ...)
def day_of_week(date):
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

# Move forward (or backward) by a number of days
def day_iter(start_date, num):
    current = start_date
    if num > 0:
        for _ in range(num):
            current = after(current)
    else:
        for _ in range(-num):
            current = before(current)
    return current

# Print usage message
def usage():
    print("Usage: assignment1.py DD/MM/YYYY +/-NN")
    exit()

# Main logic starts here
if __name__ == "__main__":
    import sys

    # Expect exactly 2 arguments: date and offset number
    if len(sys.argv) != 3:
        usage()

    input_date = sys.argv[1]
    
    # Try converting second argument to number
    try:
        offset = int(sys.argv[2])
    except:
        usage()

    # Check if date is valid
    if not valid_date(input_date):
        usage()

    # Get new date after offset
    result = day_iter(input_date, offset)

    # Print result with day of the week
    print(f"The end date is {day_of_week(result)}, {result}.")
