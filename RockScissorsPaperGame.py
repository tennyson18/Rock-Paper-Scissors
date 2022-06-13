import random

game_list = ['R', 'S', 'P'] 

while True:
    comp_input = random.choice(game_list)
    user_input = input("Welcome to rock, scissors, paper; enter R for rock, P for paper, or S for scissors: ")
    
    if user_input not in game_list:
        print('Sorry, only enter either R, S or P')
        continue
    elif user_input == comp_input:
        print('Draw\nplay again!')
        continue
    else:
        break

if comp_input == 'R' and user_input == 'S':
    print('Player (Scissors) : CPU (Rock)')
    print('Computer wins') 
    exit()
if comp_input == 'S' and user_input == 'R':
    print('Player (Rock) : CPU (Scissors)')
    print('You win!')
    exit()

if comp_input == 'P' and user_input == 'S':
    print('Player (Scissors) : CPU (Paper)')
    print('You win!')
    exit()

if comp_input == 'S' and user_input == 'P':
    print('Player (Paper) : CPU (Scissors)')
    print('Computer wins')
    exit()

if comp_input == 'P' and user_input == 'R':
    print('Player (Rock) : CPU (Paper)')
    print('Computer wins')
    exit()

if comp_input == 'R' and user_input == 'P':
    print('Player (Paper) : CPU (Rock)')
    print('You win!')
    exit()