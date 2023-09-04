feet = int(input("Please enter a measurement in ft: "))

def conversions(feet):
    inches = feet*12
    yards = feet*(1/3)
    miles = feet*0.000189394
    return inches, yards, miles

inches, yards, miles = conversions(feet)

print(f"{inches} inches\n{yards} yards\n{miles} miles")