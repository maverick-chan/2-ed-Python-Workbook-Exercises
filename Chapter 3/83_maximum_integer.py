import random

counter = 1
update = 0

random_integer = random.randint(1, 100)
max_num = random_integer

while counter < 100:
    random_integer = random.randint(1, 100)
    if random_integer > max_num:
        max_num = random_integer
        update += 1
        print(f"{max_num}\t<== Update")
    else:
        print(random_integer)
    counter += 1

print(f"The maximum value found was {max_num}")
print(f"The maximum value was updated {update} times.")