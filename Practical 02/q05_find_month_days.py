# Filename: q05_find_month_days.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 29/1/13
# Description: Prompts for year and month, and displays number of days
# in that month

#Prompt for year and month
year = int(input("Enter a year: "))
month_no = int(input("Enter month number (e.g. January is 1, Feburary 2,...): "))
month_list = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = month_list[month_no - 1]

#Determines and displays number of days
if month_no == 1 or month_no == 3 or month_no == 5 or month_no == 7 or month_no == 8 or month_no == 10 or month_no == 12:
    print(month + " " + format(year) + " has 31 days")
elif month_no == 4 or month_no == 6 or month_no == 9 or month_no == 11:
    print(month + " " + format(year) + " has 30 days")
else:
    if year % 4 == 0 and year % 100 != 0 and month_no == 2:
        print(month + " " + format(year) + " has 29 days")
    elif year % 400 == 0 and month_no == 2:
        print(month + " " + format(year) + " has 29 days")
    else:
        print(month + " " + format(year) + " has 28 days")
