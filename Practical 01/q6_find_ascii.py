# Filename: q6_find_ascii.py
# Author: Chia Xiang Rong
# Date created: 23/1/2013
# Date modified: 23/1/2013
# Description: Receives ASCII code (between 0 and 127) and displays
# its character

#Input ASCII code
code = int(input("Enter ASCII code (between 0 and 127): "))

#Find character
char = chr(code)

#Display character
print ("Character is '{0:s}".format(char) + "'")
