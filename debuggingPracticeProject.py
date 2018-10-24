import random

def transformInput(guess):
    if guess == "heads":
        return 1
    else:
        return 0
    



guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

guess = transformInput(guess)

    
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    guess = transformInput(guess)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
