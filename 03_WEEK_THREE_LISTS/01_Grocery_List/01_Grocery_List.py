#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To make a grocery list and add items.
# Author: Sudais
# Created: 19-March-2025
# Updated: 19-March-2025
#-----------------------------------------------------------------------------
print("Welcome to the Grocery List!")

# Initial grocery list
grocery_list = ['apples', 'bread', 'milk', 'eggs']
print("\nHere is your current grocery list:")
print(grocery_list)

# Adding new items to the grocery list
print("\nLet's add some new items to your grocery list.")

# User input for new items
new_item_1 = input("Enter the first item you want to add: ")
new_item_2 = input("Enter the second item you want to add: ")

# Add the items to the list
grocery_list.append(new_item_1)
grocery_list.append(new_item_2)

# Display the updated grocery list
print("\nYour updated grocery list is:")
print(grocery_list)


print("\nCongratulations on your new and updated list!")