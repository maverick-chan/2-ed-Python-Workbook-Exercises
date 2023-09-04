numbers = list(range(1, 11))
numbers_2 = list(range(1, 11))

for num_2 in numbers_2:
    print(f"\t{num_2}", end = " ")
print()

for num in numbers:
    print(f"{num}", end = " ")
    for num_2 in numbers_2:
        product = num * num_2
        print(f"\t{product}", end = " ")
    print()