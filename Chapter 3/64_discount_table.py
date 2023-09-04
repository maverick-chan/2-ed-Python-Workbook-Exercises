discounted_price = [4.95, 9.95, 14.95, 19.95, 24.95]

for num in discounted_price:
    original_price = num / 0.6
    discounted_amount = original_price * 0.4

    print(f"\nOriginal Price: ${original_price:.2f}")
    print(f"Discounted Amount: ${discounted_amount:.2f}")
    print(f"New Price: ${num:.2f}")