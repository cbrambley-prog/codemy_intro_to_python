
'''
In this script we'll be playing with if-else statements.
These statements allow you to conditionally execute code.
The syntax is if <condition1>: <code1> elif <condition2>: <code2> else: <code3>
'''

# A guessing game for a number between 1 and 10
# Input the users name
name = input("What's your name? ")

if name == "Chris" or name == "Rudie":
    guess = int(input(f"\nThanks for having me over {name}! I'm thinking of a number between 1 and 10, guess what it is. You get 5 guesses!\n\n"))
else:
    guess = int(input(f"\nWhat's up {name}. I'm thinking of a number between 1 and 10, guess what it is. You get 5 guesses!\n\n"))

number = 4 # set the number we're trying to guess
guesses = 0 # define the guess counter

while guesses < 5: 

    if guess == number:
        print(f"\nNice one {name}! You guessed right :)\n")
        break # If correct, exit the loop
    elif abs(guess - number) == 1:
        print("\nVery close!")
    else:
        print("\nNope way off. Who are you again? ")
    guess = int(input("Have another guess: "))
    guesses += 1 # For each guess, add 1 to the counter
