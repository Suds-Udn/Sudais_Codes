#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:Random number generator
# Author: Sudais
# Created: 16-March-2025
# Updated: 17-March-2025
#-----------------------------------------------------------------------------

import random

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

# Initialize the user's guess
guess = None

# Use a while loop to keep asking the user until they guess correctly
while guess != number_to_guess:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess != number_to_guess:
        print("Wrong, try again!")
    else:
        print("Correct!")

