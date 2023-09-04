import datetime

# if abs(year - 2000) % 12 == 0:
#     print(f"{year} was the year of the Dragon.")
# elif abs(year - 2001) % 12 == 0:
#     print(f"{year} was the year of the Snake.")
# elif abs(year - 2002) % 12 == 0:
#     print(f"{year} was the year of the Horse.")
# elif abs(year - 2003) % 12 == 0:
#     print(f"{year} was the year of the Sheep.")
# elif abs(year - 2004) % 12 == 0:
#     print(f"{year} was the year of the Monkey.")
# elif abs(year - 2005) % 12 == 0:
#     print(f"{year} was the year of the Rooster.")
# elif abs(year - 2006) % 12 == 0:
#     print(f"{year} was the year of the Dog.")
# elif abs(year - 2007) % 12 == 0:
#     print(f"{year} was the year of the Pig.")
# elif abs(year - 2008) % 12 == 0:
#     print(f"{year} was the year of the Rat.")
# elif abs(year - 2009) % 12 == 0:
#     print(f"{year} was the year of the Ox.")
# elif abs(year - 2010) % 12 == 0:
#     print(f"{year} was the year of the Tiger.")
# elif abs(year - 2011) % 12 == 0:
#     print(f"{year} was the year of the Hare.")

zodiac_animals = ['Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare']
current_year = datetime.datetime.now().year

year = int(input("Enter a year: "))
zodiac_index = (year - 2000) % 12

if year < current_year:
    print(f"{year} was the year of the {zodiac_animals[zodiac_index]}.")
elif year == current_year:
    print(f"{year} is the year of the {zodiac_animals[zodiac_index]}.")
else:
    print(f"{year} will be the year of the {zodiac_animals[zodiac_index]}.")