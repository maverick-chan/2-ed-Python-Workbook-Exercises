date = input("Enter a date in the form of YYYY-MM-DD: ")

separated_date = date.split('-')
year = int(separated_date[0])
month = int(separated_date[1])
day = int(separated_date[2])

if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False

calendar = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

if isLeapYear:
    calendar[2] = 29
else:
    calendar[1] = 28

if month == 12:
    if day == calendar[month]:
        year += 1
        month = 1
        next_day = 1
        print(f"The next day is: {year}-{month:2d}-{next_day:2d}")
    else:
        next_day = day + 1
        print(f"The next day is: {year}-{month:2d}-{next_day:2d}")
else:
    if day == calendar[month]:
        month += 1
        next_day = 1
        print(f"The next day is: {year}-{month:2d}-{next_day:2d}")
    else:
        next_day = day + 1
        print(f"The next day is: {year}-{month:2d}-{next_day:2d}")