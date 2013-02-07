# Filename: q01_check_even.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 29/1/13
# Description: Reads an integer and checks whether it is even

#Prompt for integer
x = int(input("Enter number: "))

#Check if even
if x % 2 == 0:
    print(format(x) + " is even")

else:
    print(format(x) + " is odd")
