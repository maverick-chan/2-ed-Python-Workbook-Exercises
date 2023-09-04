decimal_number = int(input("Enter a decimal numebr: "))

result = ''
q = decimal_number

while q > 0:
    r = q % 2
    result = str(r) + result
    q //= 2

print(f"{decimal_number} is {result} in binary.")