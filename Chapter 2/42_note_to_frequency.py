user_note = input("Enter a note: ")

notes = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.00,
}

user_note_lower = user_note.lower()
note = user_note_lower[0]
octave = int(user_note_lower[1])


for key, value in notes.items():
    if user_note_lower == key.lower():
        print(f"{value:.2f} Hz")
    elif note.lower() == key[0].lower():
        freq = value /2 ** (4-octave)
        print(f"{freq:.2f} Hz")