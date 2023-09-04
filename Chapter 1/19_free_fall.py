import math

vi = 0
height = float(input("Enter the drop height (m): "))
gravity = 9.8

def final_speed(vi, height, gravity):
    return math.sqrt((vi**2)+2*gravity*height)

print(final_speed(vi, height, gravity))