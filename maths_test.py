'''
This is a script to test your mental arithmetic
'''

from os import system
import random

name = input("Hey, what's your name? ").capitalize()
system("clear") # clear the console to stop it from being cluttered

print(f"Hey {name}, let's test your mental arithmetic!\nThere'll be 10 questions.")

q_num = 0 # define the question counter
score = 0 # remembe the score

while q_num < 10:
    var1 = random.randint(1,100) # pick a random number between 1 and 100
    var2 = random.randint(1,100)

    if random.randint(1,2) == 1: # randomly decide between addition and subtraction
        answer = int(input(f"What's {var1} plus {var2}? "))
        system("clear")
        if answer == var1 + var2:
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
    else:
        answer = int(input(f"What's {var1} minus {var2}? "))
        system("clear")
        if answer == var1 - var2:
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
    q_num += 1

print(f"\n{name}, you're total score is {score}/10.\n")
