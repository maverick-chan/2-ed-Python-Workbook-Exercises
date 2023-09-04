thirty_one_list = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
thirty_list = ['april', 'june', 'september', 'november']

while True:
    month = input("Please enter a month: ")

    if month.lower() == 'february':
        print(f"{month.title()} has 28 or 29 days.")
        break
    elif month.lower() in thirty_one_list:
        print(f"{month.title()} has 31 days.")
        break
    elif month.lower() in thirty_list:
        print(f"{month.title()} has 30 days.")
        break
    else:
        print("Please enter a valid month.")