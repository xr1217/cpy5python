# Filename: q4_print_reverse.py
# Author: Chia Xiang Rong
# Date created: 1/3/13
# Date modified: 1/3/13
# Description: Reverses the digits of an integer n.

#Define function reverse_int(n)
def reverse_int(n):
    if n < 10:
        print(n)
    else:
        print((n % 10), end="")
        reverse_int(n // 10)

x = int(input("Enter integer to be reversed: "))
print("Reversed integer is ", end="")
reverse_int(x)