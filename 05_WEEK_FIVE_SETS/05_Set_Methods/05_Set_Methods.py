#-----------------------------------------------------------------------------
# Name: Sudais
# Purpose: User interactive set methods demo (copy, pop, clear)
# Author: Sudais
# Created: 13-April-2025
#Updated: 14- April-2025
#-----------------------------------------------------------------------------

# Get user input
user_input = input("Enter numbers for the set (comma-separated): ")
data = set(map(int, user_input.split(',')))

# Copy the set
data_copy = data.copy()
print("Copy:", data_copy)

# Pop a random element
data.pop()
print("After pop:", data)

# Clear the set
data.clear()
print("After clear:", data)
