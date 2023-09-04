x = float(input("Enter a number: "))

guess = x + 10

while abs(guess*guess - x) > 10*(-12):
    guess = (guess + x/guess)/2

print(guess)