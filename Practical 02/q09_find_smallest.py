# Filename: q09_find_smallest.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 29/1/13
# Description: Uses while loop to find largest integer n such that n^2
# is greater than 12,000

n = 0
running = True
while running:
    if n*n > 12000:
        running = False
    else:
        n = n + 1

print("Smallest integer value of n such that n^2 > 12000 is " + format(n))
        
