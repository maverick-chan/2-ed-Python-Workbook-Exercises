user_input = input("Enter a position on a chessboard: ")

column = user_input.lower()[0]
row = int(user_input[1])

black = []
white = []

for ascii_value in range(97, 104, 2):
    black.append(chr(ascii_value))

for ascii_value in range(98, 105, 2):
    white.append(chr(ascii_value))

if column in black:
    if row % 2 == 0:
        print(f"{user_input} is a white square.")
    else:
        print(f"{user_input} is a black sqaure.")
elif column in white:
    if row % 2 == 0:
        print(f"{user_input} is a black sqaure.")
    else:
        print(f"{user_input} is a white square.")