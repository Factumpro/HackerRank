'''
Day 1: Interquartile Range

  https://www.hackerrank.com/challenges/s10-interquartile-range/problem
'''

'''
TEST WITH NUMPY LIB
import numpy as np
if __name__ == '__main__':
    #values = [6, 12, 8, 10, 20, 16]
    #freqs = [5, 4, 3, 2, 1, 5]
    values = [1,2,3]
    freqs = [3,2,1]   
    values = np.repeat(values, freqs)
    # array([ 6,  6,  6,  6,  6, 12, 12, 12, 12,  8,  8,  8, 10, 10, 20, 16, 16,
    #      16, 16, 16])
    values.sort()
    _half = len(values)//2
    Q1 = float( median( values[: _half] ) )
    if len(values) %2 == 0:
        Q3 = float( median( values[_half  : _half  + len(values[: _half])] ) )
    else:
        Q3 = float( median( values[_half+1: _half+1+ len(values[: _half])] ) )        
    print( round(Q3-Q1, 1) )
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#import numpy as np

from statistics import median

def interQuartile(values, freqs):
    _v = values
    _f = freqs
    #numpy function
    #values = np.repeat(values, freqs) 
    # array([ 6,  6,  6,  6,  6, 12, 12, 12, 12,  8,  8,  8, 10, 10, 20, 16, 16,
    #      16, 16, 16])
    _values = []
    for i in range(len(_f)):
        _values += [_v[i]] * _f[i]
    _values.sort()
    
    _half = len(_values)//2

    Q1 = float( median( _values[: _half] ) )

    if len(values) %2 == 0:
        Q3 = float( median( _values[_half  : _half  + len(_values[: _half])] ) )
    else:
        Q3 = float( median( _values[_half+1: _half+1+ len(_values[: _half])] ) )
        
    print(round(Q3-Q1,1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)