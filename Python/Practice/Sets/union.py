#!/usr/bin/env python3

"""
    set .union()
    ------------
    https://www.hackerrank.com/challenges/py-set-union/problem

    The .union() operator returns the union of a set and the set of elements in
    an iterable.
    Sometimes, the | operator is used in place of .union() operator, but it
    operates only on the set of elements in set.
    Set is immutable to the .union() operation (or | operation).
"""


if __name__ == '__main__':
    _, a = input(), set(input().split())
    _, b = input(), set(input().split())
    print(len(a.union(b)))
