counter = 1
active = True

while counter < 101:
    if counter % 3 == 0 and counter % 5 == 0:
        print("Fizz & Buzz")
        counter += 1
    elif counter % 3 == 0:
        print("Fizz")
        counter += 1
    elif counter % 5 == 0:
        print("Buzz")
        counter += 1
    else:
        print(counter)
        counter += 1