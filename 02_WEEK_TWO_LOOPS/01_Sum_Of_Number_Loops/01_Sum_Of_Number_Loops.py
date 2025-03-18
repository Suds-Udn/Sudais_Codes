#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:Sum of number
# Author: Sudais
# Created: 17-March-2025
# Updated: 18-March-2025
#-----------------------------------------------------------------------------

# Ask the user for a number
n = int(input("Enter a number: "))

# Initialize the sum variable
total_sum = 0

# Use a for loop to calculate the sum of numbers from 1 to n
for i in range(1, n+1):
    total_sum = total_sum+i
    print(f"Sum = {total_sum}")
