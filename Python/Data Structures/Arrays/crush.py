#!/bin/python3

import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    """
    O(n**2) - need optimization!
    """
    arr_m = [0 for _ in range(n)]    
    for i in range(len(queries)):
        ind_start = queries[i][0] - 1
        ind_end = queries[i][1]
        for j in range(ind_start, ind_end):
            arr_m[j] += queries[i][2]
    return max(arr_m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()