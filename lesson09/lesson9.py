# Lesson 9

from random import choice

invalid = True
player = ''

while invalid:
    player = input("Enter rock, paper, or scissors: ")

    if player in {'rock', 'paper', 'scissors'}:
        invalid = False

cpu = choice(['rock', 'paper', 'scissors'])
print(f"I chose {cpu}")

if player == cpu:
    print("The game is tied")
else:
    if player == 'rock':
        if cpu == 'paper':
            print("You lost")
        else:
            print("You won")
    elif player == 'paper':
        if cpu == 'scissors':
            print("You lost")
        else:
            print("You won")
    else:
        if cpu == 'rock':
            print("You lost")
        else:
            print("You won")
