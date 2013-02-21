# Filename: q1_display_reverse.py
# Author: Chia Xiang Rong
# Date created: 19/2/13
# Date modified: 19/2/13
# Description: Reverses the order of numbers in an integer.

#Define function
def reverse_int(n):
    result = 0
    while n != 0:
        rem = n % 10
        result = result * 10 + rem
        n = n // 10
    return result
        
#Prompt for input of integer
n = int(input("Enter an integer: "))
print("Reversed integer: " + str(reverse_int(n)))
