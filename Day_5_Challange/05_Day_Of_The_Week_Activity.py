print("You're going to tell me the current day of the week, and then I will provide you with an activity for each day.")
print()

day = input("Tell me the day of the week: ")

if day == "Monday":
    print("Start your week with a workout")
elif day == "Tuesday":
    print("It's a great day to read a book")
elif day == "Wednesday":
    print("Mid-week movie night!")
elif day == "Thursday":
    print("Try a new recipe")
elif day == "Friday":
    print("Relax and enjoy the weekend")
elif day == "saturday":
    print("Go for a hike!")
elif day == "sunday":
    print("Take it easy and prepare for the week ahead!")
else:
    print("Invalid input! Please enter a valid day of the week.")