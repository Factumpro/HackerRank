#!/bin/python3

import math
import os
import random
import re
import sys


def dynamicArray(n, queries):
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    result = []
    for i in range(len(queries)):
        if queries[i][0] == 1:
            seq = (queries[i][1] ^ lastAnswer) % n
            arr[seq].append(queries[i][2])
        else:
            seq = (queries[i][1] ^ lastAnswer) % n
            ind = queries[i][2] % len(arr[seq])
            lastAnswer = arr[seq][ind]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()