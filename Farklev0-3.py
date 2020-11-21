#Kean Jaycox
#Farkle v0.3
#11/20/2020

import random

#def take_your_turn():                               #will need to call rolling_dice in the take your turn func
                                                    

def rolling_dice():                                  #rough sketch of rolling dice process, NEEDS WORK
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
            i -= 1
        print("\n")

#start of the game here
print("Hello, welcome to Farkle!!!!")
numPlayers = int(input("Enter number of players: "))
rows, cols = (numPlayers, 2)
arr = [[0]*cols]*rows                                       #create correctly sized array
i = numPlayers
t = i

while i > 0:                                                #fill array with players names and score = 0
    arr[t - i] = [input("Enter player name: "),0]
    i -= 1

i = numPlayers
t = i
while i > 0:                                                #display starting score of 0 for everyone
    print(arr[t-i][0], "-----",arr[t-i][1])
    i -= 1
                                                                                #this is condition where game ends
#while arr[0][1] < 10000 and arr[1][1] < 10000 and arr[2][1] < 10000:           #if someone scores above 10000
i = numPlayers
t = 0
while t < i:                                                                    #initiating turns
    print(arr[t][0], "it's your turn!")
    #take_your_turn()                                                           #call turn func
    t += 1
