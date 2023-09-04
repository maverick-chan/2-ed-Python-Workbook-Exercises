import math

a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

def calculations (a, b):
    print(a + b)
    print(b - a)
    print(a * b)
    print(a / b)
    print(a % b)
    print(math.log(a, 10))
    print(a**b)

calculations(a, b)