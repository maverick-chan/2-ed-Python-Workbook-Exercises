wavelengths = {
    'violet': (380, 450),
    'blue': (450, 495),
    'green': (495, 570),
    'yellow': (570, 590),
    'orange': (590, 620),
    'red': (620, 750)
}

active = True

while active:
    wavelength = int(input("Enter a wavelength (nm): "))

    for key, value in wavelengths.items():
        if value[0] <= wavelength < value [1]:
            print(f"The wavelength {wavelength} nm is the colour: {key.upper()}.")
            active = False
            break
        elif wavelength == 750:
            print(f"The wavelength {wavelength} nm is the colour: RED")
            active = False
            break
        
    else:
        print("Wavelength outside the visible spectrum. Please enter a wavelength between 380 and 750 nm.")
    