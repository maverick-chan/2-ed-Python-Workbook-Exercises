mag = float(input("Enter an earthquake magnitude: "))

if mag < 2.0:
    print(f"A {mag} earthquake is considered to be a 'micro' earthquake.")
elif 2.0 <= mag < 3.0:
    print(f"A {mag} earthquake is considered to be a 'very minor' earthquake.")
elif 3.0 <= mag < 4.0:
    print(f"A {mag} earthquake is considered to be a 'minor' earthquake.")
elif 4.0 <= mag < 5.0:
    print(f"A {mag} earthquake is considered to be a 'light' earthquake.")
elif 5.0 <= mag < 6.0:
    print(f"A {mag} earthquake is considered to be a 'moderate' earthquake.")
elif 6.0 <= mag < 7.0:
    print(f"A {mag} earthquake is considered to be a 'strong' earthquake.")
elif 7.0 <= mag < 8.0:
    print(f"A {mag} earthquake is considered to be a 'major' earthquake.")
elif 8.0 <= mag < 10.0:
    print(f"A {mag} earthquake is considered to be a 'great' earthquake.")
else:
    print(f"A {mag} earthquake is considered to be a 'meteoric' earthquake.")
