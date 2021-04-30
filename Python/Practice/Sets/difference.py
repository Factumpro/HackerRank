#!/usr/bin/env python3

"""
    Set .difference()
    -----------------
    https://www.hackerrank.com/challenges/py-set-difference-operation/problem

    The tool .difference() returns a set with all the elements
    from the set that are not in an iterable.

    Sometimes the - operator is used in place of the .difference() tool, but
    it only operates on the set of elements in set.

    Set is immutable to the .difference() operation (or the - operation).
"""


if __name__ == '__main__':
    _, x1 = input(), set(input().split())
    _, x2 = input(), set(input().split())
    print(len(x1.difference(x2)))
