# Filename: q06_kilograms_to_pounds.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 30/1/13
# Description: Displays table converting kilograms to pounds for 1 kg to 10 kg

print(("{0} {1}".format("Kilograms", "Pounds")))

for x in range(1,11):
        if x < 5 or x == 10:
            print("{0} {1:>11.1f}".format(x, x * 2.2))
        else:
            print("{0} {1:>12.1f}".format(x, x * 2.2))
