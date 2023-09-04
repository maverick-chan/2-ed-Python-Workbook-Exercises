active = True
total_cost = 0

while active:
    age = input("Enter you age (or blank to quit): ")

    if age != '':
        age = int(age)
        if  age <= 2:
            total_cost += 0
        elif 3 <= age <= 12:
            total_cost += 14
        elif age >= 65:
            total_cost += 18
        else:
            total_cost += 23
    else:
        active = False

print(f"\nThe total cost for the group is: ${total_cost:.2f}")