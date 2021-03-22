'''
Set .union() Operation

  https://www.hackerrank.com/challenges/py-set-union/problem
'''

'''
The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).
'''

not_need1 =input()
a = set(input().split())
not_need2 = input()
b = set(input().split())
print(len(a.union(b)))