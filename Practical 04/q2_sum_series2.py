# Filename: q2_sum_series2.py
# Author: Chia Xiang Rong
# Date created: 1/3/13
# Date modified: 1/3/13
# Description: Computes m(i) = 1/3 + 2/5 + 3/7 + ... + i/(2i+1)

#Define function sum_series1(i)
def sum_series2(i):
    if i == 1:
        return (1/3)
    else:
        return i/(2*i + 1) + sum_series2(i-1)

x = int(input("Enter integer: "))
print("Sum of series is " + str(sum_series2(x)))