#!/bin/python3

import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    """
    O(n+m)
    """
    array = [0] * (n + 1)
    for query in queries: 
        ind_start = query[0] - 1
        ind_end = query[1]
        array[ind_start] += query[2]
        array[ind_end] -= query[2]
    max_value = 0
    count = 0
    for i in array:
        count += i
        if count > max_value:
            max_value = count
    return max_value

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