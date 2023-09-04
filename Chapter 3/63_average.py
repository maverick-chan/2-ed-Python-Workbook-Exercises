import statistics

active= True
averages = []

while active:
    value = float(input("Enter a value: "))
    if value == 0:
        active = False
    else:
        averages.append(value)
        print(f"{statistics.mean(averages):.2f}")