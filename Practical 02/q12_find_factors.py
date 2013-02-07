# Filename: q12_find_factors.py
# Author: Chia Xiang Rong
# Date created: 30/1/13
# Date modified: 7/2/13
# Description: Reads an integer and displays all its smallest factors.

#Input of integer
x = int(input("Enter an integer: "))
factors = []

#Determine and display smallest factors
i = 2
while i <= x:
    if x % i == 0:
        factors.append(i)
        x = x / i
    else:
        i = i + 1

if factors == []:
    print("No smaller factors. Integer is a prime number.")
else:
    print("Smallest factors of integer: " + format(factors))
