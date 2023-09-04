feet = int(input("Please enter a measurement in ft: "))

def conversions(feet):
    inches = feet*12
    yards = feet*(1/3)
    miles = feet*0.000189394
    return inches, yards, miles

inches, yards, miles = conversions(feet)

print(f"{inches:.2f} inches\n{yards:.2f} yards\n{miles:.2f} miles")