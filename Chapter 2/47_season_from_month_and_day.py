date = input("Enter a date (Month Day): ")

seperated_date = date.lower().split(' ')

month = seperated_date[0]
day = int(seperated_date[1])

#spring = March 20 [2] - June 20 [5]
#summer = June 21 [5] - September 21 [8]
#fall = September 22 [8] - December 20 [11]
#winter = December 21 [11] - March 19 [2]

calendar_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

index_month = calendar_months.index(month)

if (index_month == 2 and day >= 20) or (3 <= index_month <= 5) or (index_month == 5 and day <= 20):
    print(f"{date} is in spring!")
elif (index_month == 5 and day >= 21) or (6 <= index_month <= 8) or (index_month == 8 and day <= 21):
    print(f"{date} is in summer!")
elif (index_month == 8 and day >= 22) or (9 <= index_month <= 11) or (index_month == 11 and day <= 20):
    print(f"{date} is in fall!")
else:
    print(f"{date} is in winter!")