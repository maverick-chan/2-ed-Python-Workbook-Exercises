grade_conversion = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0,
}

grade = input("Enter your letter grade: ").upper()

for key, value in grade_conversion.items():
    if grade.upper() == key:
        print(f"{grade} converts to a {value}.")
        break
else:
    print("Invalid response. Please enter a valid grade.")