#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input())
    for i in range(10):
        print('{} x {} = {}'.format(n, i+1, n*(i+1)))
