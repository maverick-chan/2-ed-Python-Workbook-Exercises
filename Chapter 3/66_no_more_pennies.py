active = True
total_cost = 0

while active:
    prices = (input("Enter each purchase. Enter a blank line to stop: "))

    if prices == '':
        active = False
    else:
        total_cost += float(prices)

print(f"The exact amount payable is ${total_cost:.2f} total.")

rounding_indicator = total_cost*100 % 5

if rounding_indicator < 2.5:
    cash_total = total_cost - rounding_indicator /100
else:
    cash_total = total_cost + 0.05 - rounding_indicator /100

print(f"The cash amount payable is ${cash_total:.2f} total.")