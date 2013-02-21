# Filename: q4_sum_series.py
# Author: Chia Xiang Rong
# Date created: 19/2/13
# Date modified: 19/2/13
# Description: Computes m(i) = 1/2 + 2/3 + ... + i/(i+1) and displays results in table.

#Define function m(i)
def m_series(i):
    if i == 0:
        return 0
    else:
        return i/(i + 1) + m_series(i - 1)

#Print table
print('{0} {1:>8}'.format("i", "m(i)"))
for x in range(1, 21):
    if x < 10 or x > 12:
        print('{0} {1:>10.4f}'.format(x, m_series(x)))
    else:
        print('{0} {1:>9.4f}'.format(x, m_series(x)))
