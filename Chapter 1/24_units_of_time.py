d = int(input("Enter number of days: "))
h = int(input("Enter number of hours: "))
m = int(input("Enter number of minutes: "))
s = int(input("Enter number of seconds: "))

def seconds_conversion(d, h, m, s):
    s_in_min = m*60
    s_in_hour = h*(60**2)
    s_in_day = d*(60**2)*24
    s_in_sec = s
    return s_in_min + s_in_hour + s_in_day + s_in_sec

result = seconds_conversion(d, h, m, s)
print(f"That duration is {result} seconds long.")