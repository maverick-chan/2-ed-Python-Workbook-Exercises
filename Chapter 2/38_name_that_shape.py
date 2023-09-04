while True:
    sides = int(input("Enter the number of sides of a shape: "))

    if sides > 10:
        print("Please limit to 10 sides or less.")
    elif sides == 3:
        print(f"A {sides}-sided shape is a triangle.")
        break
    elif sides == 4:
        print(f"A {sides}-sided shape can be a square, rectangle, rhombus, trapezoid, or a parallelogram.")
        break
    elif sides == 5:
        print(f"A {sides}-sided shape is a pentagon.")
        break
    elif sides == 6:
        print(f"A {sides}-sided shape is a hexagon.")
        break
    elif sides == 7:
        print(f"A {sides}-sided shape is a heptagon.")
        break
    elif sides == 8:
        print(f"A {sides}-sided shape is a octogon.")
        break
    elif sides == 9:
        print(f"A {sides}-sided shape is a nonagon.")
        break
    elif sides == 10:
        print(f"A {sides}-sided shape is a decagon.")
        break
    else:
        print("Please enter 3 or more sides.")