# Filename: q11_find_gcd.py
# Author: Chia Xiang Rong
# Date created: 7/2/13
# Date modified: 7/2/13
# Description: Finds the greatest common divisor of two integers n1 and n2.

#Prompt for input of two integers n1 and n2
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

#Make d the minimum of the two integers
if n1 < n2:
    d = n1
else:
    d = n2

#Find greatest common divisor
running = True
while running:
    if n1 % d == 0 and n2 % d == 0:
        print("Greatest common divisor: " + format(d))
        running = False
    else:
        d = d - 1


