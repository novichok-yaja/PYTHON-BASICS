import random
import sys


a = '''


░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██████╗░░█████╗░░█████╗░██╗░░██╗░░██████╗░░█████╗░██████╗░███████╗██████╗░░░░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗░░░░
░░░░██╔══██╗██╔══██╗██╔══██╗██║░██╔╝░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗░░██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝░░░░
░░░░██████╔╝██║░░██║██║░░╚═╝█████═╝░░░██████╔╝███████║██████╔╝█████╗░░██████╔╝░░╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░░░░░
░░░░██╔══██╗██║░░██║██║░░██╗██╔═██╗ ░░██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗░░░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗░░░░
░░░░██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗░░██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║░░██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝░░░░
░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝░░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


'''
print(a)

wins = 0
losses = 0
ties = 0
computer_move = ''


def humanMove(player_move):

    if player_move == 'r':
        print('ROCK🗿 versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    return


def computerMove():

    global computer_move
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computer_move = 'r'
        print('ROCK🗿')
    elif randomNumber == 2:
        computer_move = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computer_move = 's'
        print('SCISSORS')

    return


def result(player_move, computer_move):

    global wins, losses, ties
    if player_move == computer_move:
        print('It is a tie!😌')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!😎')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!😎')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!😎')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!😬')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!😬')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!😬')
        losses = losses + 1

    return


while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    print('Enter your move: (r)ock🗿 (p)aper📃 (s)cissors✂️ or (q)uit🛑')

    player_move = input()

    if player_move == 'q':
        print("👋 👋 👋 👋 👋")
        sys.exit()

    if player_move == 'r' or player_move == 'p' or player_move == 's':
        humanMove(player_move)
        computerMove()
        result(player_move, computer_move)
    else:
        print("Select valid input 🗿 📃 ✂️")
