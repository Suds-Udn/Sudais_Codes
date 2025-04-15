#-----------------------------------------------------------------------------
# Name: Sudais
# Purpose: Creating and printing a set from user input
# Author: Sudais
# Created: 13-April-2025
# Updated: 14- April-2025
#-----------------------------------------------------------------------------

# Ask the user how many fruits they want to enter
num = int(input("How many fruits would you like to add? "))

# Create an empty set to store fruits
fruits = set()

# Loop to get fruit names from the user
for i in range(num):
    fruit = input(f"Enter fruit #{i + 1}: ").strip().lower()
    fruits.add(fruit)

# Print the final set of fruits
print("Here is your set of fruits:")
print(fruits)