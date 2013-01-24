# Filename: q5_upper_to_lower.py
# Author: Chia Xiang Rong
# Date created: 23/1/2013
# Date modified: 23/1/2013
# Description: Converts an uppercase letter from standard input to a
# lowercase letter by making use of its ASCII value

#Input of uppercase letter
char = input("Enter uppercase letter: ")

#Convert to lowercase letter
char = chr(ord(char) + 32)

#Display lowercase letter
print (char)
