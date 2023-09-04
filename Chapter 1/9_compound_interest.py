savings = int(input("Enter the amount in your savings count: "))

interest = 1.04
year = 1

while year < 4:
    savings = savings * interest
    print(savings)
    year += 1