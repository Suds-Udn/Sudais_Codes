#-----------------------------------------------------------------------------
# Name: Sudais
# Purpose: User-interactive adding and removing elements with update() and discard()
# Author: Sudais
# Created: 13-April-2025
#Updated: 14- April-2025
#-----------------------------------------------------------------------------

# Create a set of letters
letters = {'a', 'b', 'c'}

# Print the starting set
print("Starting set:", letters)

# Ask user for elements to add
add_elements = input("Enter elements to add (comma-separated): ").split(',')
letters.update([element.strip() for element in add_elements])

# Ask user which element to remove
remove_element = input("Enter element to remove: ").strip()
letters.discard(remove_element)

# Print the updated set
print("Updated set:", letters)
