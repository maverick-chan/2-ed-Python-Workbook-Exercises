while True:
    human_age = int(input("Enter your age: "))
    if human_age < 0:
        print("Please enter a valid age.")
    elif human_age <= 2:
        dog_age = human_age * 10.5
        print(f"You are {dog_age} years old in dog years.")
        break
    else:
        dog_age = 2*10.5 + (human_age-2)*4
        print(f"You are {dog_age} years old in dog years.")
        breakhuman_age = int(input("Enter your age: "))