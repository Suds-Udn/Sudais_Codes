#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To help people decide what to do on each day of the week
# Author: Sudais
# Created: 4-March-2025
# Updated: 4-March-2025
#-----------------------------------------------------------------------------
#Providing user information of what this code will do
print("You're going to tell me the current day of the week, and then I will provide you with an activity for each day.")
print()
#Save what day of the week it as a variable called day
day = input("Tell me the day of the week: ") #Keeping the user input as a variable

#If variable Monday with a response
if day == "Monday": #Anwser regaring the user input
    print("Start your week with a workout")

#If variable Tuesday with a response
elif day == "Tuesday":
    print("It's a great day to read a book")

#If variable Wednesday with a response
elif day == "Wednesday":
    print("Mid-week movie night!")

#If variable Thursday with a response
elif day == "Thursday":
    print("Try a new recipe")

#If variable Friday with a response
elif day == "Friday":
    print("Relax and enjoy the weekend")

#If variable Saturday with a response
elif day == "saturday":
    print("Go for a hike!")

#If variable Sunday with a response
elif day == "sunday":
    print("Take it easy and prepare for the week ahead!")

# If input is uncorrect with a response
else:
     print("Invalid input! Please enter a valid day of the week.")