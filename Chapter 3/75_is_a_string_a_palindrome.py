user_string = input("Enter a word: ")

def palindrome_check(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

print(palindrome_check(user_string))
