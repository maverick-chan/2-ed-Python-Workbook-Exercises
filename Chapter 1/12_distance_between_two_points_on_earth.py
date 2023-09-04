import math

coordinate_1 = input("Please enter the first coordinate: ")
coordinate_2 = input("Please enter the second coordinate: ")

coordinate_1 = [substring.strip() for substring in coordinate_1.split(',')]
coordinate_2 = [substring.strip() for substring in coordinate_2.split(',')]


t1, g1 = coordinate_1
t2, g2 = coordinate_2

t1 = math.radians(float(t1))
g1 = math.radians(float(g1))
t2 = math.radians(float(t2))
g2 = math.radians(float(g2))

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))
print(f"The distance between these two points is: {distance} km")

#----------------------------------------

import math

coordinate_1 = input("Please enter the first coordinate: ")
coordinate_2 = input("Please enter the second coordinate: ")

t1, g1 = map(math.radians, map(float, coordinate_1.split(',')))
t2, g2 = map(math.radians, map(float, coordinate_2.split(',')))

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(f"The distance between these two points is: {distance} km")
