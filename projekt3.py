from colors import bcolors
import random
import os
from msvcrt import getwch
from time import sleep 
from rps_def import hand, user_input, scissors, rock, paper, exit_game, newgame

wins = 0
losses = 0
ties = 0
turns = 0
keys = ["R", "P", "S", "Q", "N"]
os.system('cls')

newgame()

while True: 
    ai = random.randint(1,3)
    print(bcolors.PURPLE+"Choose Rock, Paper or Scissors (R, P, S or Q for quit and N for new game)")
    user = getwch().upper() #gör så att man kan använda både stora och små bokstäver
    if user in keys:
        turns = turns + 1
        os.system('cls') # suddar ut allt man skrivit innan
        print(bcolors.CYAN+f"AI chose {hand(ai)}")
        if ai == 1: # ai == 1,2,3 är funktioner till användning av händerna
            rock()
        elif ai == 2:
            paper()
        else:
            scissors()
        print(bcolors.BLUE+f"You chose: {user_input(user)}")
        if user == 'R': #här printas sten ut ifall spelaren trycker på R
            rock()
        elif user == 'P': #här printas påse ut ifall spelaren trycker på P
            paper()
        else:
            scissors()
            
        if user_input(user) == hand(ai): #här betyder det att om båda till exempel får sten så blir det lika
            print(bcolors.YELLOW+"Tie")
            ties = ties + 1
            print(f"{bcolors.DEFAULT}You have wins: {wins} | Ties: {ties} | Losses: {losses} | Turns: {turns}")

        elif user == "R": #här väljer användaren sten och ai sax så då vinner användaren
            if hand(ai) == "Scissors":
                print(bcolors.GREEN+"You won this round")
                wins += 1
                print(f"{bcolors.DEFAULT}You have wins: {wins} | Ties: {ties} | Losses: {losses} | Turns: {turns}")
            else:
                print(bcolors.RED+"You lost this round") #om ai tar påse så vinner ai och användaren förlorar
                losses += 1
                print(f"{bcolors.DEFAULT}You have wins: {wins} | Ties: {ties} | Losses: {losses} | Turns: {turns}")

        elif user == "S": #här väljer användaren sax och ai påse så då vinner användaren
            if hand(ai) == "Paper":
                print(bcolors.GREEN+"You won this round")
                wins += 1
                print(f"{bcolors.DEFAULT}You have wins: {wins} | Ties: {ties} | Losses: {losses} | Turns: {turns}")
            else:
                print(bcolors.RED+"You lost this round") #om ai tar sten så vinner ai och användaren förlorar
                losses += 1
                print(f"{bcolors.DEFAULT}You have wins: {wins} | Ties: {ties} | Losses: {losses} | Turns: {turns}")

        elif user == "P": #här väljer användaren papper och ai sten så då vinner användaren
            if hand(ai) == "Rock":
                print(bcolors.GREEN+"You won this round")
                wins = wins + 1
                print(f"{bcolors.DEFAULT}You have wins: {wins} | Ties: {ties} | Losses: {losses} | Turns: {turns}")
            else: 
                print(bcolors.RED+"You lost this round") #om ai tar sax så vinner ai och användaren förlorar
                losses += 1
                print(f"{bcolors.DEFAULT}You have wins: {wins} | Ties: {ties} | Losses: {losses} | Turns: {turns}")
            
        elif user == "N": #om användaren trycker på N så startas ett nytt spel
           newgame()

        if user == "Q": #om användaren trycker Q så avslutas spelet
            exit_game()
            sleep(1)
            exit()