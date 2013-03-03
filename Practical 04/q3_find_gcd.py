# Filename: q3_find_gcd.py
# Author: Chia Xiang Rong
# Date created: 1/3/13
# Date modified: 1/3/13
# Description: Finds the greatest common divisor of two numbers

#Define function gcd(m, n)
def gcd(m, n):
    if m == 0:
        return n
    elif n == 0:
        return m
    return gcd(n, (m % n))

#Determine gcd of 24, 16 and 255, 25
print(gcd(24, 16))
print(gcd(255, 25))
