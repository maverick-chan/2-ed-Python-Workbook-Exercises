counter = 1

pi = 3
print(f"Approximation {counter}: {pi}")
while counter <= 14:
    if counter % 2 != 0:
        x = counter * 2
        pi = pi + 4/(x*(x+1)*(x*2))
        print(f"Approximation {counter + 1}: {pi}")
        counter += 1
    else:
        x = counter * 2
        pi -= 4/(x*(x+1)*(x*2))
        print(f"Approximation {counter + 1}: {pi}")
        counter += 1