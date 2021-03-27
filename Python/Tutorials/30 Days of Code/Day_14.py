#!/usr/bin/env python3


class Difference:
    def __init__(self, a):
        self.elements = a
        self.difference = 0

    def max_difference(self):
        self.difference = max(self.elements) - min(self.elements)
        return self.difference

if __name__ == '__main__':
    arg = list(map(int, input().split(" ")))
    diff = Difference(arg)
    print(diff.max_difference())
