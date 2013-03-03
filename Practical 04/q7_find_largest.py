# Filename: q7_find_largest.py
# Author: Chia Xiang Rong
# Date created: 3/3/13
# Date modified: 3/3/13
# Description: Returns the largest integer in an array alist

#Create list and prompt input of integers
alist = []
x = int(input("Enter number of integers: "))
for i in range(0,x):
    num = int(input("Enter integer: "))
    alist.append(num)

#Define function find_largest(alist)
def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        if alist[0] > alist[1]:
            alist[1] = alist[0]
        return find_largest(alist[1:])
    
print("Largest integer is: " + str(find_largest(alist)))
