# Filename: q04_determine_leap_year.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 29/1/13
# Description: Prompts for year and determines whether it is a leap year.

#Prompt for year
year = int(input("Enter year: "))

#Determine whether year is leap year and display result
if year % 4 == 0 and year % 100 != 0:
    print("Leap year!")
elif year % 400 == 0:
    print("Leap year!")
else:
    print("Non-leap year...")
