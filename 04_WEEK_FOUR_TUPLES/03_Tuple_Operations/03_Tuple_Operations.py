#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose: See the amount of repetition
# Author: Sudais
# Created: 27-March-2025
# Updated: 28-March-2025
#-----------------------------------------------------------------------------

#Create a tuple with repeated values
fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")

#Ask the user to enter a fruit name
fruit_name = input("Enter a fruit name: ")

#Print how many times that fruit appears in the tuple
count = fruit_tuple.count(fruit_name)
print(f"'{fruit_name}' appears {count} times in the tuple.")