# Filename: q8_find_uppercase.py
# Author: Chia Xiang Rong
# Date created: 3/3/13
# Date modified: 3/3/13
# Description: Finds number of uppercase letters in a string.

#Define function find_num_uppercase(str)
def find_num_uppercase(string):
    if len(string) == 1:
        if ord(string[0]) >= 65 and ord(string[0]) <= 90:
            return 1
        return 0
    else:
        if ord(string[0]) >= 65 and ord(string[0]) <= 90:
            return 1 + find_num_uppercase(string[1:])
        return 0 + find_num_uppercase(string[1:])

string2 = input("Enter string: ")
print("Number of uppercase letters in string: " + str(find_num_uppercase(string2)))
