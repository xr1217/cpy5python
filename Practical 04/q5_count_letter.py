# Filename: q5_count_letter.py
# Author: Chia Xiang Rong
# Date created: 1/3/13
# Date modified: 1/3/13
# Description: Finds the number of occurrences of a specified letter ch in a string str.

#Define function count_letter(str, ch)
def count_letter(str,ch):
    if(len(str) == 1):
        return (str == ch)
    else:
        return (str[0] == ch) + count_letter(str[1:],ch)

#Prompt input of string and letter
string = str(input("Enter string: "))
letter = str(input("Enter letter to be searched: "))
print("Occurance of letter: " + str(count_letter(string,letter)))
