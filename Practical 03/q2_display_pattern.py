# Filename: q2_display_pattern.py
# Author: Chia Xiang Rong
# Date created: 21/2/13
# Date modified: 21/2/13
# Description: Displays pattern where a right-aligned triangle with n columns/rows is printed

#Define function display_pattern(n)
def display_pattern(n):
    prev_num = []
    for i in range(1, n + 1):
        prev_num.insert(0, str(i) + " ")
    length = len("".join(prev_num))
    prev_num = []

    for j in range(1,n+1):
        prev_num.insert(0, str(j) + " ")
        print("{0:>s}".format(("".join(prev_num))).rjust(length))


x = int(input("Enter an integer: "))
display_pattern(x)

