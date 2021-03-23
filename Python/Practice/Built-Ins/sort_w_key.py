'''
Athlete Sort

  https://www.hackerrank.com/challenges/python-sort-sort/problem

  arr.sort(key=lambda x: f(x))
  print(*arr)
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def sort_krow(x,k):
    return x[k]

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key=lambda x: sort_krow(x,k))

for row in arr:
    print(*row)
