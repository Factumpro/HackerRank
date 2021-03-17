'''
Bubble Sort

'''

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
sort_index = 0
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j +1]:
            a[j], a[j +1] = a[j +1], a[j]
            sort_index +=1
print('Array is sorted in {} swaps.'.format(sort_index))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))