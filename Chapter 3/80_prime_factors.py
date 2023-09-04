integer = int(input("Enter an integer (2 or greater): "))

if integer < 2:
    print("Invalid input. Please enter an integer that is 2 or greater.")
else:
    factor = 2
    print(f"The prime factors of {integer} are:")
    while factor <= integer:
        if integer % factor == 0:
            print(factor)
            integer /= factor
        else:
            factor += 1