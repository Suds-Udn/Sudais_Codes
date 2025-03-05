#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To help people know if they can vote or not
# Author: Sudais
# Created: 3-March-2025
# Updated: 4-March-2025
#-----------------------------------------------------------------------------
print ("Its voting time! Lets see if you are eligable!")
print ()
age=int(input("Tell me your age than I will tell you if you can vote")) #Storing the vote as a variable

if age >=18: #Anwser regaridng the user input
    print ("You are eligible to vote!")

elif age <18:
    print ("Sorry you cant vote, you are not the eligible age")