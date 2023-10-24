'''
Guess the number game using python.
'''

import random


guess_digit = random.randint(0,101)

print(guess_digit)

while True:
    guess_number = input('Please guess the number from 1 - 100: ')
    if guess_number.isdigit():
        if int(guess_number) == int(guess_digit):
            print('You guessed it right!')
            break
        else:
            print('Wrong. Try again!')
    else:
        print('You put an invalid number.',end=' ') 
        print('Please choose a number from 1 to 100.')
