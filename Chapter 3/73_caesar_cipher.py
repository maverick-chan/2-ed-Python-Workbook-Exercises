import string
alphabet_string = string.ascii_lowercase
alphabet_lower = list(alphabet_string)
alphabet_upper = list(alphabet_string.upper())

def encoder(message):
    encoded_message = []
    for char in message:
        if char in alphabet_lower:
            index = alphabet_lower.index(char)
            if index >= 23:
                encoded_message.append(alphabet_lower[index - 23])
            else:        
                encoded_message.append(alphabet_lower[index + 3])
        elif char in alphabet_upper:
            index = alphabet_upper.index(char)
            if index >= 23:
                encoded_message.append(alphabet_upper[index - 23])
            else:        
                encoded_message.append(alphabet_upper[index + 3])
        else:
            encoded_message.append(char)

    separator = ""
    encoded_result = separator.join(encoded_message)
    print(f"Your encoded message is: {encoded_result}")
    return encoded_result

def decoder(encoded_message):
    decoded_message = []
    for char in encoded_message:
        if char in alphabet_lower:
            index = alphabet_lower.index(char)
            if index >= 23:
                decoded_message.append(alphabet_lower[index + 23])
            else:        
                decoded_message.append(alphabet_lower[index - 3])
        elif char in alphabet_upper:
            index = alphabet_upper.index(char)
            if index >= 23:
                decoded_message.append(alphabet_upper[index + 23])
            else:        
                decoded_message.append(alphabet_upper[index - 3])
        else:
            decoded_message.append(char)

    separator = ""
    decoded_result = separator.join(decoded_message)
    print(f"Your decoded message is: {decoded_result}")
    return decoded_result

def main():
    message = input("Enter a message: ")
    encoded = encoder(message)
    decoded = decoder(encoded)

main()