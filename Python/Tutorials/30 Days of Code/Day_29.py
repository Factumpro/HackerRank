#!/usr/bin/env python3

import math
import os
import random
import re
import sys


def bitwiseAnd(N, K):
    max_value = 0
    for i in range(1, N+1):
        for j in range(1, i):
            if max_value == K-1:
                return max_value
            value = i & j
            if value > max_value and K > value:
                max_value = value

    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for _ in range(int(input().strip())):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        res = bitwiseAnd(count, lim)
        fptr.write(str(res) + '\n')
    fptr.close()
