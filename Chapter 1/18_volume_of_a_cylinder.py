import math

r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

def volume(r, h):
    return (math.pi * (r**2)) * h

print(volume(r, h))