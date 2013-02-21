# Filename: q7_display_matrix.py
# Author: Chia Xiang Rong
# Date created: 19/2/13
# Date modified: 19/2/13
# Description: Displays n by n matrix, where n is a positive integer entered
# by user. Each element is 0 or 1, generated randomly.

import random
def print_matrix(n):
    for i in range(0, n):
        for x in range (0, n):
            print(random.randint(0,1), end=" ")
        print(" ")

x = int(input("Enter an integer: "))
print_matrix(x)
