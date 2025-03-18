#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To slice a list and find its length.
# Author: Sudais
# Created: 19-March-2025
# Updated: 19-March-2025
#-----------------------------------------------------------------------------
print("Welcome to the Color List!")

# Initial colors list
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print("\nHere is your current list of colors:")
print(colors)

# Slicing the list to get the second and third colors
sliced_colors = colors[1:3]  # This will get 'blue' and 'green'
print("\nThe second and third colors in the list are:")
print(sliced_colors)

# Finding the length of the colors list
list_length = len(colors)
print("\nThe total number of colors in your list is:")
print(list_length)

print("\nThank you for using the Color List!")