#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To calculate what grade people got regarding there mark in a Ontario Level
# Author: Sudais
# Created: 28-February-2025
# Updated: 4-March-2025
#-----------------------------------------------------------------------------

print("Hello, let's calculate what grade you got together!")
print()

score = int(input("Write your score (out of 100): "))
print()
print()

if score >= 90:
    print("Congratulations! You have gotten a 4+, keep up the good work!")
elif score >= 87 and score < 94:
    print("Congratulations! You have achieved level 4!")
elif score >= 86 and score < 87:
    print("Congratulations! You have achieved level 4-")
elif score >= 77 and score < 86:
    print("Congratulations! You have gotten a level 3+")
elif score >= 74 and score < 77:
    print("You have gotten a level 3. Keep up the good work!")
elif score >= 70 and score < 74:
    print("Congratulations! You got a level 3-")
elif score >= 67 and score < 70:
    print("Good job! You got a level 2+")
elif score >= 64 and score < 67:
    print("Good job! You got a level 2")
elif score >= 60 and score < 64:
    print("Good job! You got a level 2-")
elif score >= 57 and score < 60:
    print("You got a level 1+. Practice more!")
elif score >= 54 and score < 57:
    print("You got a level 1. Better luck next time!")
elif score >= 50 and score < 54:
    print("You got a level 1-. Better luck again!")
if score < 0 or score > 100:
    print("Invalid score. Please enter a valid score between 0 and 100.")
