# Filename: q6_compute_sum.py
# Author: Chia Xiang Rong
# Date created: 3/3/13
# Date modified: 3/3/13
# Description: Computes sum of digits in an integer.

#Define function sum_digits(n)
def sum_digits(n):
    if (n < 10):
        return n
    else:
        return n % 10 + sum_digits(n // 10)

#Prompt input of integer
integer = int(input("Enter integer: "))
print("Sum of digits in integer: " + str(sum_digits(integer)))
