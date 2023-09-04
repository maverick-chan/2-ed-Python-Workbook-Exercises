from random import randrange

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 11, 10, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

value = randrange(0, 38)
if value == 37:
    print("The spin resulted in 00...")
else:
    print(f"The spin resulted in {value}")
    
if value == 37:
    print("Pay 00")
else:
    print("Pay", value)

    if value in red:
        print("Pay Red")
    elif value in black:
        print("Pay Black")
    else:
        print("Print Green")

    if value % 2 == 0:
        print("Pay Even")
    else:
        print("Pay Odd")
    
    if 1 <= value <= 18:
        print("Pay 1 to 18")
    elif 19 <= value <= 36:
        print("Pay 18 to 36")