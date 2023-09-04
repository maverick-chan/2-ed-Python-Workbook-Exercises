binary_string = (input("Enter a binary number: "))

decimal = 0
power = 0

for digit in reversed(binary_string):
    if digit == '1':
        decimal += 2 ** power
    power += 1

print(f"The decimal equivalent of {binary_string} is {decimal}")