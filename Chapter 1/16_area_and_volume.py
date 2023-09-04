import math

r = int(input("Please enter a radius: "))

def area(r):
    ar = math.pi*(r**2)
    return ar

def volume(r):
    vol = 4/3*math.pi*(r**3)
    return vol

print(area(r))
print(volume(r))