number = input("Enter three numbers separated by commas: ")

number_list = number.split(',')
integer_list = [float(item) for item in number_list]
sorted_integers = sorted(integer_list)

print(sorted_integers)

