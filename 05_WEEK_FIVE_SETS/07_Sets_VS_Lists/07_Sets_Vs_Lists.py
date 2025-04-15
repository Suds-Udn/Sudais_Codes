#-----------------------------------------------------------------------------
# Name: Sudais
# Purpose: User-interactive set vs list demo
# Author: Sudais
# Created: 13-April-2025
#Updated: 14- April-2025
#-----------------------------------------------------------------------------

# Ask user to input a list of numbers with possible duplicates
user_input = input("Enter numbers for the list: ")
num_list = [int(x.strip()) for x in user_input.split(',')]

# Convert the list to a set
num_set = set(num_list)

# Print both the list and set
print("List:", num_list)
print("Set:", num_set)
