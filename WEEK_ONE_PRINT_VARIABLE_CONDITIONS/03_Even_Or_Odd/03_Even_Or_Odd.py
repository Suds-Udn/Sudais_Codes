#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose: To tell people weather a number is even or odd
# Author: Sudais
# Created: 2-March-2025
# Updated: 4-March-2025
#-----------------------------------------------------------------------------
#informing user the purpose
print ("Hello today I will help you to figure out if a number is even or odd? Tell me a number and I will tell you if its even or odd!")
print ()
# Stored the number as a variable
number= int(input ("Please tell me your number"))
#if number is %2 ==0 with response
if number % 2 ==0:
    print("Your number is even")
#if number is %2but ==1 with a response
elif number % 2 == 1:
    print("Your number is odd")
#if number %22 but ==2 with a response
elif number % 2 ==2:
    print("Your number is even")
#if number format is wrong with response
else:
    print("The number you wrote is not correct")
