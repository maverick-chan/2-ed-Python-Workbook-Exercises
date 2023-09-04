while True:
    birthday = input("Enter your birthday (Month Day): ")

    separated_birthday = birthday.lower().split(' ')
    if len(separated_birthday) != 2:
        print("Invalid input. Please enter the date in the format 'Month Day'.")
    else:
        month = separated_birthday[0]
        day = int(separated_birthday[1])
        break

calendar_months = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december'
}

reversed_calendar_months = {value: key for key, value in calendar_months.items()}

index_month = reversed_calendar_months[month]
    
if(index_month == 1 and day >= 2) or (index_month == 2 and day <= 18):
    print("Your astrological sign is an Aquarius!")
elif(index_month == 2 and day >= 19) or (index_month == 3 and day <= 20):
    print("Your astrological sign is an Pisces!")
elif(index_month == 3 and day >= 21) or (index_month == 4 and day <= 19):
    print("Your astrological sign is an Aries!")
elif(index_month == 4 and day >= 20) or (index_month == 5 and day <= 20):
    print("Your astrological sign is an Taurus!")
elif(index_month == 5 and day >= 21) or (index_month == 6 and day <= 20):
    print("Your astrological sign is an Gemini!")
elif(index_month == 6 and day >= 21) or (index_month == 7 and day <= 22):
    print("Your astrological sign is an Canacer!")
elif(index_month == 7 and day >= 23) or (index_month == 8 and day <= 22):
    print("Your astrological sign is an Leo!")
elif(index_month == 8 and day >= 23) or (index_month == 9 and day <= 22):
    print("Your astrological sign is an Virgo!")
elif(index_month == 9 and day >= 23) or (index_month == 10 and day <= 22):
    print("Your astrological sign is an Libra!")
elif(index_month == 10 and day >= 22) or (index_month == 11 and day <= 21):
    print("Your astrological sign is an Scorpio!")
elif(index_month == 11 and day >= 22) or (index_month == 12 and day <= 21):
    print("Your astrological sign is an Sagitarius!")
else:
    print("Your astrological sign is an Aquarius!")