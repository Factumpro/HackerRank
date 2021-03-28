#!/usr/bin/env python3

"""
    Exceptions - String to Integer
    ------------------------------

    The `try` statement may have more than one
    `except` clause, and we need to define only ValueError.

    https://docs.python.org/3/tutorial/errors.html (8.3. Handling Exceptions)

    'ValueError: Could not convert data to an integer.'
"""

import sys

if __name__ == '__main__':
    try_str = input().strip()
    try:
        print(int(try_str))
    except ValueError:
        print("Bad String")
