#Kean Jaycox
#Dice Random 005
#roll 1 - 6 die until exit

import random
val = 0                                             #declare val
print("Instructions:\n--Enter number of dice to roll (1 - 6)\n--Press 'e' to exit\n")
while(val != 'e'):
    val = input()                                   #user chooses
    if val != 'e':                                  #choice, exit or rolling
        i = int(val)                                #typecast so while loop accepts i as int
    total = 0
    while(0 < i < 7):
        r = random.randint(1,6)                     #rand int 1 - 6
        print(r, '', end = '')
        total = total + r
        i -= 1
    if total != 0:
        print("\ntotal =", total, "\n")
