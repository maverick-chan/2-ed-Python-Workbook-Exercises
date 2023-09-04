change = float(input("Enter you change: "))

coins = {
    2.00: "toonie",
    1.00: "loonie",
    0.25: "quarter",
    0.10: "dime",
    0.05: "nickel",
    0.01: "penny",
}

values = [2.00, 1.00, 0.25, 0.10, 0.05, 0.01]

index = 0
while change != 0 and index < len(values):
    factor = change // values[index]
    print(f"{int(factor)} {coins[values[index]]}")
    remaining = change % values[index]
    change = remaining
    index += 1

#--------------------------------------------------------
change = float(input("Enter you change: "))

coins = {
    2.00: "toonie",
    1.00: "loonie",
    0.25: "quarter",
    0.10: "dime",
    0.05: "nickel",
    0.01: "penny",
}

for value in coins.keys():
    if change >= value:
        factor = change // value
        print(f"{int(factor)} {coins[value]}")
        remaining = change % value
        change = remaining