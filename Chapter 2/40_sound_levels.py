sound_level = int(input("Enter a sounds level in dB: "))

noises = {
    'Quiet Room': 40,
    'Alarm Clock': 70,
    'Gas Lawnmower': 106,
    'Jackhammer': 130,
}

reversed_noises = {values: keys for keys, values in noises.items()}

for key, value in noises.items():
    if sound_level == value:
        print(f"The sound level corresponds to: {key}")
        break
    elif sound_level < value:
        print(f"The sound level is quieter than: {key}")
        break
    elif 40 < sound_level < 70:
        print(f"The sound level is between {reversed_noises[40]} and {reversed_noises[70]}.")
        break
    elif 70 < sound_level < 106:
        print(f"The sound level is between {reversed_noises[70]} and {reversed_noises[106]}.")
        break
    elif 106 < sound_level < 130:
        print(f"The sound level is between {reversed_noises[106]} and {reversed_noises[130]}.")
        break
else:
    print(f"The sound is louder than: Jackhammer")