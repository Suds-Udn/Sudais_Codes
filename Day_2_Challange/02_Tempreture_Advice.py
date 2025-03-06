#-----------------------------------------------------------------------------
# Name:Sudais
# Purpose:To help people know what to wear outside
# Author: Sudais
# Created: 1-March-2025
# Updated: 4-March-2025
#-----------------------------------------------------------------------------
#Asking user info for anwser
print ("What is the temperature outside")
print ()
# Informing use of code
print ("I will help you dress accordingly to the weather")
# Storing the temperature as a variable
temperature = int(input ("What is the temperature"))
#if temp less than 10 degree with response
if temperature <=10:
    print ("Its cold outside make sure to dress properly and stay warm!")
#elif temp 10-25 degree with response
elif temperature <= 10 and temperature <= 25:
    print ("Its nice weather go out have fun and enjoy the day")
#elif 25 or more degree with response
elif temperature >=25:
    print ("It is very hot try to stay undoor and dont forget your sunscreen!")
