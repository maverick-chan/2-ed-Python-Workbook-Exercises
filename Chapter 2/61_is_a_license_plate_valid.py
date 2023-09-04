license_plate = input("Enter you license plate (using '-' as the separator): ")

separated_license_plate = license_plate.split('-')
first_half = separated_license_plate[0]
second_half = separated_license_plate[1]

if len(license_plate) == 7:
    if first_half.isalpha() and second_half.isdigit():
        print(f"{license_plate} is a valid license plate.")
    else:
        print("Invalid license plate.")
elif len(license_plate) == 8:
    if first_half.isalpha() and second_half.isdigit():
        print(f"{license_plate} is a valid license plate.")
    else:
        print("Invalid license plate.")
else:
    print("Invalid license plate.")