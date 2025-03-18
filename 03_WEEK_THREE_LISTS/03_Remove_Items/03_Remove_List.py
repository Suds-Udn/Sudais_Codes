#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To remove an item from a list.
# Author: Sudais
# Created: 19-March-2025
# Updated: 19-March-2025
#-----------------------------------------------------------------------------
print("Welcome to the To Do List!")

# Initial to-do list
todo_list = ['write email', 'finish homework', 'call mom', 'clean room']
print("\nHere is your current to-do list:")
print(todo_list)

# Removing 'call mom' from the list
print("\nLet's remove 'call mom' from your to-do list.")
todo_list.remove('call mom')

# Display the updated list after removing 'call mom'
print("\nYour updated to-do list is:")
print(todo_list)

# Removing 'clean room' from the list
print("\nNow, let's remove 'clean room' from your to-do list.")
todo_list.remove('clean room')

# Display the final to-do list after removing 'clean room'
print("\nYour final to-do list is:")
print(todo_list)

print("\nThank you and stay orginized!")