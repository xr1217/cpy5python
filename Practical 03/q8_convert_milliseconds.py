# Filename: q8_convert_milliseconds.py
# Author: Chia Xiang Rong
# Date created: 20/2/13
# Date modified: 20/2/13
# Description: Converts milliseconds to hours, minutes and seconds.

#Define convert_ms(n)
def convert_ms(n):
    hours = n // 3600000
    n = n - (3600000 * hours)
    minutes = n // 60000
    n = n - (60000 * minutes)
    seconds = n // 1000
    print("Time in hours, minutes, seconds is " + str(hours) + ":" + str(minutes) + ":" + str(seconds))

#Prompt for milliseconds
i = int(input("Enter number of milliseconds: "))
convert_ms(i)
        
