#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To use list comprehensions to filter and manipulate data based on a condition.
# Author: Sudais
# Created: 19-March-2025
# Updated: 19-March-2025
#-----------------------------------------------------------------------------
print("Welcome to the Number List Manager!")

# Initial list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nHere is your list of numbers:")
print(numbers)

# Using list comprehension to filter even numbers from the numbers list
even_numbers = [num for num in numbers if num % 2 == 0]
print("\nThe even numbers from the list are:")
print(even_numbers)

# Using list comprehension to square each of the even numbers
squared_numbers = [num ** 2 for num in even_numbers]
print("\nThe squares of the even numbers are:")
print(squared_numbers)

print("\nThank you for using the Number List!")