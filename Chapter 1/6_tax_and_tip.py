meal_cost = float(input("Please input the cost of your meal: "))
tax = meal_cost * 0.12
tip = meal_cost * 0.18
total = meal_cost + tax + tip

print("Meal: $%.2f, \nTax: $%.2f, \nTip: $%.2f, \nTotal: $%.2f" % (meal_cost, tax, tip, total))

meal_cost = float(input("Please input the cost of your meal: "))
tax = meal_cost * 0.12
tip = meal_cost * 0.18
total = meal_cost + tax + tip

print(f"Meal: ${meal_cost:.2f}, \nTax: ${tax:.2f}, \nTip: ${tip:.2f}, \nTotal: ${total:.2f}")
