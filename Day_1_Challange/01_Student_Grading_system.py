#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To calculate what grade people got regarding there mark in a Ontario Level
# Author: Sudais
# Created: 28-February-2025
# Updated: 4-March-2025
#-----------------------------------------------------------------------------

print("Hello, let's calculate what grade you got together!") #Start Explain user what we will be calculating
print()

score = int(input("Write your score (out of 100): ")) #Storing the score in the input User puts his mark
print()
print()

#If user scores a 90 or above with the response
if score >= 90:
    print("Congratulations! You have gotten a 4+, keep up the good work!")
# Elif user gets 94-87 with the response
elif score >= 87 and score < 94:
    print("Congratulations! You have achieved level 4!")
#Elif user gets 87-86 with the response
elif score >= 86 and score < 87:
    print("Congratulations! You have achieved level 4-")
# Elif user gets 86-77 with the response
elif score >= 77 and score < 86:
    print("Congratulations! You have gotten a level 3+")
#Elif user gets a 70-74 with the response
elif score >= 74 and score < 77:
    print("You have gotten a level 3. Keep up the good work!")
#Elif user gets a 70-74 with response
elif score >= 70 and score < 74:
    print("Congratulations! You got a level 3-")
#Elif user gets 67-70 with response
elif score >= 67 and score < 70:
    print("Good job! You got a level 2+")
#Elif user gets 64 - 67 with response
elif score >= 64 and score < 67:
    print("Good job! You got a level 2")
#Elif user gets 60-64 with response
elif score >= 60 and score < 64:
    print("Good job! You got a level 2-")
#elif user gets 57-60 with response
elif score >= 57 and score < 60:
    print("You got a level 1+. Practice more!")
#Elif user gets a 54 - 57 with a response
elif score >= 54 and score < 57:
    print("You got a level 1. Better luck next time!")
#Elif user gets 50-54 with respone
elif score >= 50 and score < 54:
    print("You got a level 1-. Better luck again!")
#If user puts a number other than 0-100 with response
if score < 0 or score > 100:
    print("Invalid score. Please enter a valid score between 0 and 100.")
