# Filename: q5_compute_series.py
# Author: Chia Xiang Rong
# Date created: 19/2/13
# Date modified: 19/2/13
# Description: Computes m(i) = 4(1 - 1/3 + ... + 1/(2i - 1) - 1/(2i + 1)) and displays results in table.

#Define function m(i)
def m(i):
    if i == 1:
        return 8/3
    else:
        return (4/(2 * i - 1) - 4/(2 * i + 1)) + m(i - 2)
    
#Print table
print('{0} {1:>8}'.format("i", "m(i)"))
for x in range(1, 20, 2):
    if x < 10:
        print('{0} {1:>17.11f}'.format(x, m(x)))
    else:
        print('{0} {1:>16.11f}'.format(x, m(x)))
