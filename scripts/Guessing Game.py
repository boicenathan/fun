### Number Guessing Game ###

import random

number = random.randrange(1, 100)

guess = int(input('Guess a number between 1 and 100: '))

while guess != number:
    if guess > number:
        print('Your guess is too high.')
        guess = int(input('Guess a number between 1 and 100: '))

    else:
        print('Your guess is too low.')
        guess = int(input('Guess a number between 1 and 100: '))

print('Your guess is correct!  Thanks for playing!')
