#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To help people know what to wear outside
# Author: Sudais
# Created: 1-March-2025
# Updated: 4-March-2025
#-----------------------------------------------------------------------------

print ("What is the temperature outside")
print ()
print ("I will help you dress accordingly to the weather")
temperature = int(input ("What is the temperature")) # Storing the temperature as a variable


if temperature <=10: # Possible outputs considering the user input
    print ("Its cold outside make sure to dress properly and stay warm!")
elif temperature <= 10 and temperature <= 25:
    print ("Its nice weather go out have fun and enjoy the day")
elif temperature >=25:
    print ("It is very hot try to stay undoor and dont forget your sunscreen!")
