import random

num = random.randint(1, 101)
counter = 0
print('Welcome to the guessing number game \nI thought of a number - you need to guess it')

def is_valid(guess):
    return guess.isdigit() and 1 <= int(guess) <= 100

def guessing():
    while True:
        guess = input('Enter your guess: ')
        if is_valid(guess):
            return int(guess)
        else:
            print('Any chance you enter any number between 1 and 100?')

while True:
    guess = guessing()
    counter +=1
    if num > guess:
        print('Your number is smaller, try one more time')
        continue
    elif num < guess:
        print('Your number is bigger, try one more time')
        continue
    else:    
        print('Correct, congrats, you won, what a surprise!')
        break

print(f'Game stats:\nYou did {counter} attempts')
print('Thanks for playing, see you soon...')
