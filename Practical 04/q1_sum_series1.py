# Filename: q1_sum_series1.py
# Author: Chia Xiang Rong
# Date created: 1/3/13
# Date modified: 1/3/13
# Description: Computes m(i) = 1 + 1/2 + 1/3 + ... + 1/i

#Define function sum_series1(i)
def sum_series1(i):
    if i == 1:
        return 1
    else:
        return 1/i + sum_series1(i-1)

x = int(input("Enter integer: "))
print("Sum of series is " + str(sum_series1(x)))
