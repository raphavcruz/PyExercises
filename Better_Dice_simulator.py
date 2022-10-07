# Dice_simulator. The goal of this project is to simulate the use of two 6-sided dices, generating a value from 1 to 6 and matching said value in both virtual dices

#import library
import random
import PySimpleGUI

chances_to_play = 0

print("Auto dice number matching")
print("Your goal is to get the same number in both virtual dices")
print("How many changes you want to play??\n")

n=input()

while chances_to_play<int(n):
    
    input("Press ENTER key to roll dices:")

    chances_to_play = chances_to_play + 1

    # The randint() method returns an integer number selected element from the specified range

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print(dice1, dice2)


    if dice1==dice2:
     print("You Win!\n")
    
     break

else:

    print("Not win")

    # f-Strings are a new way of string formatting

    print(f"{int(n) - chances_to_play} chances left out of {int(n)}\n")

print("Game Over")