#!/usr/bin/env python3

"""
    Athlete Sort
    ------------
    https://www.hackerrank.com/challenges/python-sort-sort/problem

    arr.sort(key=lambda x: f(x))
    print(*arr)
"""


def ksort_row(x, k):
    return x[k]


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    _ = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr.sort(key=lambda x: ksort_row(x, k))
    for row in arr:
        print(*row)
