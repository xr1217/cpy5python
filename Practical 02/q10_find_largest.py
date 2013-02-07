# Filename: q10_find_largest.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 29/1/13
# Description: Uses while loop to find largest integer such that n^3 is
# less than 12,000

n = 0
running = True

while running:
    if n*n*n < 12000:
        n = n + 1
    else:
        n = n - 1
        running = False

print("Largest integer value of n such that n^3 is less than 12,000 is " + format(n))
