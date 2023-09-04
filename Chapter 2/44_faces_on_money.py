banknotes = {
    'George Washington': 1,
    'Thomas Jefferson': 2,
    'Abraham Lincoln': 5,
    'Alexander Hamilton': 10,
    'Andrew Jackson': 20,
    'Ulysses S. Grant': 50,
    'Benjamin Franklin': 100,
}

denomination = int(input("Enter a banknote amount: "))

for key, value in banknotes.items():
    if denomination == value:
        print(f"A ${value} bill has the face of {key} on it.")
        break
else:
    print("You have enter an invalid banknote amount.")