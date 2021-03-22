'''
Introduction to Sets

  https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

'''

'''
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
'''

def average(array):
    array=set(array)
    array=list(array)
    return (sum(array))/len(array)