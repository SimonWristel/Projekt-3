import os
def hand(ai): #ai är programerad att välja mellan 1 till 3 och om ai väljer 1 så blir det omgjort till sten
    if ai == 1:
        return "Rock"
    elif ai == 2:
        return "Paper"
    elif ai == 3:
        return "Scissors"
    
def user_input(user): #om användaren väljer R så blir det omgjort till Rock
    if user =="R":
        return "Rock"
    elif user == "P":
        return "Paper"
    elif user == "S":
        return "Scissors"


def newgame(): 
    global wins, losses, turns, ties
    wins = 0
    losses = 0
    turns = 0 
    ties = 0
    os.system('cls')
    print("""
 ____            _      ____                       
|  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __ 
| |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__|
|  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |   
|_|_\_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_| 
 ____   
/ ___|  ___(_)___ ___  ___  _ __ _|_|              
\___ \ / __| / __/ __|/ _ \| '__/ __|              
 ___) | (__| \__ \__ \ (_) | |  \__ \              
|____/ \___|_|___/___/\___/|_|  |___/  
       """)
    
def scissors():
    print(""" 
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
\__SCISSORS___/\n""")

def rock():
    print("""   
   _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/\n""")

def paper():
    print("""
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/\n""")

def exit_game():
    print("""
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \ 
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\     *   )   )               )      (               / /\ 
/ /\ \  ` )  /(( /(    )       ( /(      )\ )     (     / /\ \ 
\ \/ /   ( )(_))\())( /(  (    )\())(   (()/(  (  )(    \ \/ /
 \/ /   (_(_()|(_)\ )(_)) )\ )((_)\ )\   /(_)) )\(()\    \/ / 
 / /\   |_   _| |(_|(_)_ _(_/(| |(_|(_) (_) _|((_)((_)   / /\ 
/ /\ \    | | | ' \/ _` | ' \)) / /(_-<  |  _/ _ \ '_|  / /\ \ 
\ \/ /    |_| |_||_\__,_|_||_||_\_\/__/  |_|_\___/_|    \ \/ /
 \/ /          (                         |   /           \/ / 
 / /\          )\   ) (   (        (  (  |  /            / /\ 
/ /\ \   `  ) ((_| /( )\ ))\  (    )\))( | /            / /\ \ 
\ \/ /   /(/(  _ )(_)|()/((_) )\ )((_))\ |/             \ \/ /
 \/ /   ((_)_\| ((_)_ )(_)|_)_(_/( (()(_|                \/ / 
 / /\   | '_ \) / _` | || | | ' \)) _` |)\               / /\ 
/ /\ \  | .__/|_\__,_|\_, |_|_||_|\__, ((_)             / /\ \ 
\ \/ /  |_|           |__/        |___/                 \ \/ /
 \/ /                                                    \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \ 
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' """)