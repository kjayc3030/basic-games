#Kean Jaycox
#Dice Random 003

import random
val = 'z'

while(val != 'e'):
    val = input("Instructions:\n--Press 'r' to roll two dice\n--Press 'e' to exit\n")
    if val == 'r':
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        total = r1 + r2
        print(r1, r2, ' = ', total)

