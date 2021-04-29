#!/usr/bin/env python3

_, x1 = input(), set( input().split())
_, x2 = input(), set( input().split())
print(*sorted(x1.symmetric_difference(x2), key=int), sep='\n')