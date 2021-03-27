#!/usr/bin/env python3

import os
import re
import sys
import math
import random
import operator
import functools as fun


def factorial(Num):
    if Num == 1:
        return Num
    else:
        return Num*factorial(Num-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    Num = int(input())
    result = factorial(Num)

    fptr.write(str(result) + '\n')
    fptr.close()
