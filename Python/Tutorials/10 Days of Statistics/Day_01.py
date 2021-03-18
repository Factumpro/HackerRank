'''
10/Day 1: Quartiles

  Given an array, arr, of n integers, calculate the respective 
  first quartile (),
  second quartile (), and 
  third quartile ().
  It is guaranteed that, all are integers.

sorted
find half = len(arr[len(arr)//2)

!!! upper half len == lower half len

first quartile  - lower half (left):     int median( arr[: half] )
second quartile - median (center):       int median( arr )
third quartile  - upper half (right): 
                    if len(arr) %2 == 0: int median( arr[half  : half  + len(arr[: half])] )
                    if len(arr) %2 != 0: int median( arr[half+1: half+1+ len(arr[: half])] )
'''

'''
Example 1

  arr = [1,3,5,7]
  sorted = arr
  lower half is [1, 3] = 2
  median of the entire array is [3, 5] = 4
  upper half is [5, 7] = 6

  [2, 4, 6]

Example 2

  arr = [9,5,7,1,3]
  sorted = [1, 3, 5, 7, 9]
  lower half is [1, 3] = 2
  median of the entire array is [5] = 5
  upper half is [7, 9] = 8

  [2, 5, 8]

Example 3

  arr = [3, 7, 8, 5, 12, 14, 21, 13,18]
  sorted = [3, 5, 7, 8, 12, 13, 14, 18, 21]
  lower half is [3, 5, 7, 8] = 6
  median of the entire array is [12] = 12
  upper half is [13, 14, 18, 21] = 16

  [6, 12, 16]
'''

'''
TEST 

if __name__ == '__main__':

  n = 9
  arr = [3, 7, 8, 5, 12, 14, 21, 13,18]
  #arr = [9,5,7,1,3]
  #arr = [1,3,5,7]
  arr.sort()

  if len(arr) %2 == 0:
      print(arr[:(len(arr)//2)])
      print( arr[ (len(arr)//2) : ( (len(arr)//2) + len( arr[:(len(arr)//2)] )) ] )

      print( str(int(median( arr[: (len(arr)//2) ] ))))
      print(str( int(median(arr)) ))  
      print( str(int(median( arr[ (len(arr)//2) : ( (len(arr)//2) + len( arr[:(len(arr)//2)] )) ] ) )) )      
  else:
      print(arr[:(len(arr)//2)])
      print( arr[ (len(arr)//2)+1 : ( (len(arr)//2)+1 + len( arr[:(len(arr)//2)] )) ] )

      print( str(int(median( arr[: (len(arr)//2) ] ))))
      print(str( int(median(arr)) ))  
      print( str(int(median( arr[ (len(arr)//2)+1 : ( (len(arr)//2)+1 + len( arr[:(len(arr)//2)] )) ] )) ))  
'''
#!/bin/python3

import math
import os
import random
import re
import sys

from statistics import median

def quartiles(arr):
    _arr = arr
    _arr.sort()
    _half = len(_arr)//2
    Q1 = int(median( _arr[: _half] ))
    Q2 = int(median( _arr ))
    if len(_arr) %2 == 0:
        Q3 = int(median( _arr[_half  : _half  + len(arr[: _half])] ))
    else:
        Q3 = int(median( _arr[_half+1: _half+1+ len(arr[: _half])] ))
    return Q1,Q2,Q3
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()