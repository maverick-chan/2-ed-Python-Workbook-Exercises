import math

a = float(input("Enter the 'a' value: "))
b = float(input("Enter the 'b' value: "))
c = float(input("Enter the 'c' value: "))

def quadratic_function(a, b, c):
    discriminant = math.sqrt((b**2) - 4*a*c)
    if discriminant < 0:
        print("The quadratic equation does not have any real roots.")
    elif discriminant == 0:
        root_0 = -b/(2*a)
        print(f"The quadratic equation has one real root, {root_0}.")
    else:
        root_1 = (-b + discriminant)/ (2*a)
        root_2 = (-b - discriminant)/ (2*a)
        print(f"The quadratic equation has two real roots, {root_1} and {root_2}")