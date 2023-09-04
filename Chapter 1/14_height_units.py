feet = int(input("Please enter you height (ft): "))
inches = int(input("Please enter you height (inches): "))

def centimeter_conversion(feet, inches):
    inches_1 = feet*12
    total_inches = inches + inches_1
    centimeter = total_inches * 2.54
    return centimeter

result = centimeter_conversion(feet, inches)
print(result)