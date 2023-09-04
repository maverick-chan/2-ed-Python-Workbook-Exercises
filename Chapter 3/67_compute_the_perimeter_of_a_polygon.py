import math

active = True
x_points = []
y_points = []
perimeter = 0

while active:
    x_coord = input("Enter the next x-coordinate (blank to quit): ")

    if x_coord != '':
        y_coord = input("Enter the next y-coordinate: ")
        x_points.append(float(x_coord))
        y_points.append(float(y_coord))

        if len(x_points) > 1:
            index = len(x_points) - 1          
            distance = math.sqrt((x_points[index] - x_points[index - 1])**2 + (y_points[index] - y_points[index - 1])**2)
            perimeter += distance
    else:
        index = len(x_points) - 1
        distance = math.sqrt((x_points[index] - x_points[0])**2 + (y_points[index] - y_points[0])**2)
        perimeter += distance
        active = False

print(f"The perimeter of that polygon is: {perimeter:.2f}")