'''
Day 16: Exceptions - String to Integer

  !!! It's import to understand that the try statement 
      may have more than one except clause, 
      and we need to define only ValueError.

  8.3. Handling Exceptions
  https://docs.python.org/3/tutorial/errors.html

  From example:

    except ValueError:
        print("Could not convert data to an integer.")
'''


#!/bin/python3

import sys


S = input().strip()
try:
  print(int(S))
except ValueError:
  print("Bad String")