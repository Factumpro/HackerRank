#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n %2 == 0 and n not in range (6, 21):
        print ("Not", end=" "),
    print("Weird")