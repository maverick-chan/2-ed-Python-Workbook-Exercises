grade_point = float(input("Enter a grade point: "))

if grade_point >= 4.0:
    print("Your letter grade is: A+")
elif 3.7 < grade_point < 4.0:
    print("Your letter grade is: A")
elif 3.3 < grade_point <= 3.7:
    print("Your letter grade is: A-")
elif 3.0 < grade_point <= 3.3:
    print("Your letter grade is: B+")
elif 2.7 < grade_point <= 3.0:
    print("Your letter grade is: B")
elif 2.3 < grade_point <= 2.7:
    print("Your letter grade is: B-")
elif 2.0 < grade_point <= 2.3:
    print("Your letter grade is: C+")
elif 1.7 < grade_point <= 2.0:
    print("Your letter grade is: C")
elif 1.3 < grade_point <= 1.7:
    print("Your letter grade is: C-")
elif 1.0 < grade_point <= 1.3:
    print("Your letter grade is: D+")
elif 0 < grade_point <= 1.0:
    print("Your letter grade is: D")
else:
    print("Your letter grade is: F")

#------------------------------------------
grade_point = float(input("Enter a grade point: "))

grade_ranges = {
    (4.0, float('inf')): 'A+',
    (3.7, 4.0): 'A',
    (3.3, 3.7): 'A-',
    (3.0, 3.3): 'B+',
    (2.7, 3.0): 'B',
    (2.3, 2.7): 'B-',
    (2.0, 2.3): 'C+',
    (1.7, 2.0): 'C',
    (1.3, 1.7): 'C-',
    (1.0, 1.3): 'D+',
    (0.0, 1.0): 'D',
    (-float('inf'), 0.0): 'F'
}

for key, value in grade_ranges.items():
    if grade_point >= 4.0:
        print("Your letter grade is: A+")
        break
    elif key[0] < grade_point <= key[1]:
        print(f"Your letter grade is: {value}")
        break