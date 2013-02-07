# Filename: q07_miles_to_kilometres.py
# Author: Chia Xiang Rong
# Date created: 30/1/13
# Date modified: 30/1/13
# Description: Displays conversion of miles to kilometres from 1 mile to
# to 65 miles in two tables side by side.

print("{0} {1} {2} {3}".format("Miles", "Kilometres", "Miles", "Kilometres"))

i = 20
for x in range(1,11):
    if x > 6 and x < 10:
        print("{0} {1:>10.3f} {2:>6} {3:>9.3f}".format(x, x * 1.609, i, i * 1.609))
        i = i + 5
    elif x == 10:
        print("{0} {1:>9.3f} {2:>6} {3:>10.3f}".format(x, x * 1.609, i, i * 1.609))
        i = i + 5
    else:
        print("{0} {1:>9.3f} {2:>7} {3:>9.3f}".format(x, x * 1.609, i, i * 1.609))
        i = i + 5
