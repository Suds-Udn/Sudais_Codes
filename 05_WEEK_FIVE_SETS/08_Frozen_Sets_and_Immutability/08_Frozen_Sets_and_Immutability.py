#-----------------------------------------------------------------------------
# Name: Sudais
# Purpose: User-interactive frozenset demo with immutability check
# Author: Sudais
# Created: 13-April-2025
# Updated: 14- April-2025
#-----------------------------------------------------------------------------

# Ask user to input elements for the frozenset
user_input = input("Enter numbers for the frozenset")
user_set = set(map(int, user_input.split(',')))

# Create a frozenset
frozen_numbers = frozenset(user_set)

# Try to add an element (this will raise an error)
try:
    frozen_numbers.add(6)
except AttributeError as e:
    print(f"Error: {e}")

# Print the frozenset
print("Frozen set:", frozen_numbers)
