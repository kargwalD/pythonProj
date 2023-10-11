#import random
#
# def guess(x):
#     while guess != x :
#         guess = random.randint(min, max)
#
#
# min = 0
# max = 10
# random_number = int(input(f'Enter a number for the computer to guess between {min} and {max}'))
# guess(random_number)


import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess = low #or high, this is done because random.randint shows an error if the low and high are the same value


        feedback = input(f'Is {guess} too high(H), too low(L) or correct(C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Correct, the computer guessed you number {guess} correctly!!")

computer_guess(10)