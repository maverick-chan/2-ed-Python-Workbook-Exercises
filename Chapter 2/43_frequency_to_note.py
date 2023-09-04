user_frequency = float(input("Enter a frequency: "))

notes = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.00,
}

frequency_tolerance = 1.0

for key, value in notes.items():
    if abs(user_frequency - value) <= frequency_tolerance:
        print(f"The frequency you entered corresponds to note: {key}")