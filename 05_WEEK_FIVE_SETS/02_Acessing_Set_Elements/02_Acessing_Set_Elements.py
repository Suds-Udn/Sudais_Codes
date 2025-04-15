#-----------------------------------------------------------------------------
# Name: Sudais
# Purpose: Accessing and printing elements from a user-defined set
# Author: Sudais
# Created: 13-April-2025
#Updated: 14-April-2025
#-----------------------------------------------------------------------------

# Ask the user how many colors they want to enter
num = int(input("How many colors would you like to add? "))

# Create an empty set to store colors
colors = set()

# Loop to collect colors from the user
for i in range(num):
    color = input(f"Enter color #{i + 1}: ").strip().lower()
    colors.add(color)

# Print each color from the set
print("\nHere are the unique colors you entered:")
for color in colors:
    print(color)
