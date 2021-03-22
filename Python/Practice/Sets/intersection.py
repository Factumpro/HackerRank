'''
Set .intersection() Operation

  https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
'''

'''
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).
'''

_, x = input(), set( input().split())
_, y = input(), set( input().split())
print(len(x.intersection(y)))