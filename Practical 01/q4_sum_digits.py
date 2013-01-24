# Filename: q4_sum_digits.py
# Author: Chia Xiang Rong
# Date created: 22/1/2013
# Date modified: 22/1/2013
# Description: Adds all the digits in an integer between 0 to 1000

#Prompt for integer between 0 to 1000
x = int(input("Enter an integer between 0 to 1000: "))

#Check if integer is between 0 to 1000
if x <= 0 or x >= 1000:
    print ("Please enter an integer between 0 to 1000!")
    
else:

#Extract digits
    a = x % 1000 // 100
    b = x % 100 // 10
    c = x % 10

#Add digits and display result
print (a + b + c)

