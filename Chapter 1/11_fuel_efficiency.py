american_units = int(input("Please enter your fuel efficiency: "))
# 1 MPG = 0.00425144 L/100km
conversion = 0.00425144

canadian_units = american_units * conversion
print(f"Your fuel efficiency in km/L is {canadian_units} L/100km.")