active = True
sequence = []

while active:
    n = int(input("Enter any positive integer: "))
    sequence.append(n)
    if n > 0:
        while sequence[-1] != 1:
            if sequence[-1] % 2 == 0:
                next_term = sequence[-1] // 2
                sequence.append(next_term)
            else:
                next_term = (sequence[-1] * 3) + 1
                sequence.append(next_term)
        print(sequence)                
    else:
        break