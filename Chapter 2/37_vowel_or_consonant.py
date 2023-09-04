letter = input("Please enter a letter: ")

vowels = ['a', 'e', 'i', 'o', 'u']

if letter.lower() in vowels:
    print(f"'{letter.lower()}' is a vowel.")
elif letter.lower() == 'y':
    print(f"'{letter.lower()}' is sometimes a vowel, and sometimes a consonant.")
else:
    print(f"'{letter.lower()}' is a consonant.")