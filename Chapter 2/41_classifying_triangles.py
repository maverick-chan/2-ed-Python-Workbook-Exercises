triangle_lengths = input("Input the three lengths of a triangle separated by a ',': ")

items = triangle_lengths.split(',')
lengths_list = [int(item) for item in items]
len1, len2, len3 = lengths_list

if len1 == len2 == len3:
    print("The triangle you have entered is an: equilateral")
elif len1 != len2 != len3:
    print("The triangle you have entered is a: scalene")
else:
    print("The triangle you have entered is an: isosceles")