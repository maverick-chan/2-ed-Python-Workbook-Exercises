n = int(input("Enter a positive integer: "))
m = int(input("Enter another positive integer: "))

d = min(n, m)

while d % m != 0 or d % n != 0:
    d = d - 1

print(f"{d} is the greatest common divisior of {n} and {m}.")