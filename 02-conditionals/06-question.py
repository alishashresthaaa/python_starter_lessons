# Create a simple "guess the number" game.
# The program should randomly select a number between 1 and 10
# and then prompt the user to guess the number.
# Use a while loop to keep the game running until
# the user guesses correctly. After each guess,
# the program should print "Too high" or "Too low"
# if the guess is incorrect.

import random
number = random.randint(1, 10)
print("Try to guess the number between 1 to 10")
attempts = 0

while True:
    try:
        user_input = int(input("Enter your guessed number: "))
        attempts += 1
        if number == user_input:
            print("You guessed the number in {attempts} attempts")
            break
        elif user_input < number:
            print("The number is too low")
        else:
            print("The number is too high")
    except ValueError:
        print("Please enter a valid number")

