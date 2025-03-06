#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To help people know if they can vote or not
# Author: Sudais
# Created: 3-March-2025
# Updated: 4-March-2025
#-----------------------------------------------------------------------------
#Providing user what we will be doing
print ("Its voting time! Lets see if you are eligable!")
print ()
#store the input in a varibale called age
age=int(input("Tell me your age than I will tell you if you can vote")) #Storing the age as a variable

# if age is 18 or less with a response
if age >=18:
    print ("You are eligible to vote!")
#if age is more than 18 with a response
elif age <18:
    print ("Sorry you cant vote, you are not the eligible age")