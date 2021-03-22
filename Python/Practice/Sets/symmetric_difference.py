'''
Set .symmetric_difference() Operation

  https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

'''

'''
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

'''

_, x1 = input(), set( input().split())
_, x2 = input(), set( input().split())
print(len(x1.symmetric_difference(x2)))
