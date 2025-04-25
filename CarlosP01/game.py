#this a game to guess a num.

#first import random
import random
from curses.ascii import isdigit

num_guess = random.randint(1, 100)
attempt = 1

print('Welcome to guess a number game!!!')

while True:

    guess = input('Enter a number: ')

    if not guess.isdigit():
        print('Enter a valid number!')
        continue

    number = int(guess)

    attempt += 1

    if number > num_guess:
        print('Try a lower number!')
    elif number < num_guess:
        print('Try a higher number!')

    elif number == num_guess:
        print(f"congratulation you guessed the {num_guess}" )
        break




