#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:10 - 0 Countdown
# Author: Sudais
# Created: 18-February-2025
# Updated: 18-March-2025
#-----------------------------------------------------------------------------

# Start the countdown from 10
count = 10

# Use a while loop for the countdown
while count > 0:
    # Print the current countdown number
    print(count)

    # Ask the user if they want to stop
    user_input = input('Enter "stop" to cancel or press Enter: ')

    # If the user enters "stop", break the loop
    if user_input.lower() == 'stop':
        print("Countdown stopped!")
        break

    # Decrease the countdown number
    count -= 1


