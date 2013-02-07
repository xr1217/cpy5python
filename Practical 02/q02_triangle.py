# Filename: q02_triangle.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 29/1/13
# Description: Reads an three edges of a triangle and determines
# if input are valid (the sum of any two edges is greater than the third edge)
# and compute perimeter of triangle if input is valid.

#Input of sides
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

#Determine if input is valid
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle!")
else:
    print("Perimeter = {0:.2f}".format(a + b + c))
