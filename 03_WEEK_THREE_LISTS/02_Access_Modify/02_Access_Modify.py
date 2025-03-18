#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To modify a grocery list by changing an existing item.
# Author: Sudais
# Created: 19-March-2025
# Updated: 19-March-2025
#-----------------------------------------------------------------------------
print("Welcome to the Grocery List!")

# Initial grocery list
grocery_list = ['apples', 'bananas', 'carrots', 'milk', 'bread']
print("\nHere is your current grocery list:")
print(grocery_list)

# Modifying an item in the list
print("\nLet's change 'bananas' to 'Grapes' in your list.")

# Change 'bananas' to 'grapes'
grocery_list[1] = 'Grapes'

# Display the updated grocery list
print("\nYour updated grocery list is:")
print(grocery_list)

# Accessing and printing the third item
third_item = grocery_list[2]
print("\nThe third item in your grocery list is:")
print(third_item)

print("\n Thank you see you next time!")