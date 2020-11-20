#Kean Jaycox
#Dice Random 001

import random
val = 'z'
print("Instructions:\n--Enter number of dice to roll (1 - 6)\n--Press 'e' to exit\n")
while(val != 'e'):
    val = input()
    if val == '6':
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        r3 = random.randint(1,6)
        r4 = random.randint(1,6)
        r5 = random.randint(1,6)
        r6 = random.randint(1,6)
        total = r1 + r2 + r3 + r4 + r5 + r6
        print(r1, r2, r3, r4, r5, r6, ' = ', total)
    if val == '5':
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        r3 = random.randint(1,6)
        r4 = random.randint(1,6)
        r5 = random.randint(1,6)
        total = r1 + r2 + r3 + r4 + r5
        print(r1, r2, r3, r4, r5, ' = ', total)
    if val == '4':
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        r3 = random.randint(1,6)
        r4 = random.randint(1,6)
        total = r1 + r2 + r3 + r4
        print(r1, r2, r3, r4, ' = ', total)
    if val == '3':
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        r3 = random.randint(1,6)
        total = r1 + r2 + r3
        print(r1, r2, r3, ' = ', total)
    if val == '2':
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        total = r1 + r2
        print(r1, r2, ' = ', total)
    if val == '1':
        r1 = random.randint(1,6)
        total = r1
        print(r1)

