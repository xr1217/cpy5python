# Filename: q6_determine_prime.py
# Author: Chia Xiang Rong
# Date created: 19/2/13
# Date modified: 19/2/13
# Description: Determines if integer is prime number and displays first 1000
# prime numbers, with 10 in each row

#Define function is_prime(n)
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for x in range(2, int(n ** 0.5) + 1, 1):
        if n % x == 0:
            return False
    return True

#Print out first 1000 prime numbers in rows of 10
a = 0
i = 0
while a < 1000:
    if is_prime(a) == True:
        print(str(a), end=" ")
        i = i + 1
        if i == 10:
            print(end = "\n")
            i = 0
    a = a + 1

    
