import random

def play():
    user = input("'r' for rock, 'p' for paper and 's' for scissors. Enter your choice: ")

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s; s > p; p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You Lost :('

def is_win(player, opponent):
    #returns true if player won
    # r > s; s > p; p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())