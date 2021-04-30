#!/usr/bin/env python3

"""
    Set .add()
    ----------
    https://www.hackerrank.com/challenges/py-set-add/problem

    If we want to add a single element to an existing set,
    we can use the .add() operation.
    It adds the element to the set and returns 'None'.
"""


if __name__ == '__main__':
    arr = set([])
    for _ in range(int(input())):
        arr.add(input())
    print(len(arr))
