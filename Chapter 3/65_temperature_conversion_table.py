#temp in F = (temp in C * 9/5) + 32

celsius = range(10, 101, 10)
celsius_list = list(celsius)

print("Celsius(°C)\tFahrenheit(°F)")
for num in celsius_list:
    fahrenheit = (num * 9/5) + 32
    print(f"{num}°C\t\t{fahrenheit}°F")