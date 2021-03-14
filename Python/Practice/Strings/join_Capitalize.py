''''
Capitalize!

  Link to problem statement:
  https://www.hackerrank.com/challenges/capitalize/problem

  You are asked to ensure that the first and last names of people begin with 
  a capital letter in their passports. For example, alison heck should be 
  capitalised correctly as Alison Heck.

  Given a full name, your task is to capitalize the name appropriately.
''''


''''
TEST

if __name__ == '__main__':
    s = 'aa bb cc 12ddd'
    print ( ' '.join(map(str.capitalize, s.split(' '))) ) 

''''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
