#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    print(sorted(list(map(len,'{0:b}'.format(int(input().strip())).split("0"))),        
    reverse=True)[0])
