minutes = int(input("Enter the number of minutes used: "))
texts = int(input("Enter the number of texts sent: "))

base_cost = 15
add_charge = 0.44
sales_tax = 1.05

if minutes > 50:
    add_min = (minutes - 50) * 0.25
else: 
    add_min = 0

if texts > 50:
    add_text = (texts - 50) * 0.15
else:
    add_text = 0

total_bill = (base_cost + add_charge + add_min + add_text) * sales_tax
tax = (base_cost + add_charge + add_min + add_text) * 0.05

print(f"Base Charge: ${base_cost:.2f}")
print(f"Additional Minutes: ${add_min:.2f}")
print(f"Additional Texts: ${add_text:.2f}")
print(f"Additional Charge: ${add_charge:.2f}")
print(f"Sales Tax: ${tax:.2f}")
print(f"Total Bill: ${total_bill:.2f}")