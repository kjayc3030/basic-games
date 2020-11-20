#Kean Jaycox
#Dice Random 001

import random
die_one = [1, 2, 3, 4, 5, 6]
n = random.randint(1,6)
val = 'z'

while(val != 'e'):
    val = input("Instructions:\n--Press 'r' to roll two dice\n--Press 'e' to exit\n")
    if val == 'r':
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        total = r1 + r2
        print(r1, r2, ' = ', total)

