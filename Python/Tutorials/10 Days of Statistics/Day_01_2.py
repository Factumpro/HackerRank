'''
10/Day 1: Standard Deviation

from statistics import median

sort
mean
sum map a[i] - mean **2 
sqrt sum_map / len_arr
round ,1
'''

'''
TEST

if __name__ == '__main__':

    #arr =[10, 40, 30, 50, 20]
    #arr = [2,5,2,7,4]

    _arr = arr
    _arr.sort()
    _len_arr = len(_arr)
    
    _mean_arr = sum(arr)/ _len_arr
    _square_summ = sum(map(lambda x: (x - _mean_arr)**2, _arr))
    
    _stdDev = math.sqrt(_square_summ/_len_arr)
    print( round(_stdDev, 1) )
'''
import math

#!/bin/python3

import math
import os
import random
import re
import sys

def stdDev(arr):
    _arr = arr
    _arr.sort()
    _len_arr = len(_arr)
    
    _mean_arr = sum(arr)/ _len_arr
    _square_summ = sum(map(lambda x: (x - _mean_arr)**2, _arr))
    
    _stdDev = math.sqrt(_square_summ/_len_arr)
    print( round(_stdDev, 1) )
    # Print your answers to 1 decimal place within this function

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
