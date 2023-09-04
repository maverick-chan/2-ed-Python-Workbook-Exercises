import random
import statistics

simulation = 1
flip_record = []

while simulation <= 10:
    active = True
    record = []
    
    flips = 0

    while active:
        random_integer = random.randint(1, 2)
        record.append(random_integer)
        flips += 1

        if len(record) >= 3 and random_integer == record[-2] and random_integer == record[-3]:  
            if random_integer == 1:
                print('H ', end='')
            elif random_integer == 2:
                print('T ', end='')
            flip_record.append(flips)  
            print(f"({flips} flips)")
            active = False
            simulation += 1

        else:
            if random_integer == 1:
                print('H ', end='')
            elif random_integer == 2:
                print('T ', end='')      
            

print(f"\nOn average, {statistics.mean(flip_record)} flips were needed")
