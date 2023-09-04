s = int(input("Enter number of seconds: "))

time = {
    "days": 86400,
    "hours": 3600,
    "minutes": 60,
    "seconds": 1

}

dictionary = {}

for key, value in time.items():
    if s >= value:
        factor = s//value
        dictionary[key]=factor
        remaining = s % value
        s = remaining

print(f"{dictionary['days']:02d}:{dictionary['hours']:02d}:{dictionary['minutes']:02d}:{dictionary['seconds']:02d}")

print(dictionary)
#D:HH:MM:SS