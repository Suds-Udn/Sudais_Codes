#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:swaping numbers
# Author: Sudais
# Created: 27-March-2025
# Updated: 28-March-2025
#-----------------------------------------------------------------------------

#Ask the user to input two numbers
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

#Store them in a tuple
numbers_tuple = (first_number, second_number)

#Swap their values
first_number, second_number = second_number, first_number

#Print the swapped values
print("Swapped values:", (first_number, second_number))