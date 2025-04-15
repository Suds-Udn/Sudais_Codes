#-----------------------------------------------------------------------------
# Name: Sudais
# Purpose: Performing set operations with user input
# Author: Sudais
# Created: 13-April-2025
# Updated: 14-April-2025
#-----------------------------------------------------------------------------

# Get input for set1
set1_input = input("Enter elements for Set 1: ")
set1 = set(map(int, set1_input.split(',')))

# Get input for set2
set2_input = input("Enter elements for Set 2: ")
set2 = set(map(int, set2_input.split(',')))

# Perform set operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

# Print results
print("\nUnion:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)
