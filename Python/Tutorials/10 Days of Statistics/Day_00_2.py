'''
Day 0: Weighted Mean

  https://www.hackerrank.com/challenges/s10-weighted-mean/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here    
    _sum_xw = sum(list(map(int, [X[i]*W[i] for i in range(len(X))])))
    _sum_w = sum(W)
    return print(round((_sum_xw/_sum_w),1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)