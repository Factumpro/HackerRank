#!/usr/bin/env python3

"""
    Task
    ----
    Given a base-10 integer, Num, convert it to binary (base-2).
    Then find and print the base-10 integer denoting the maximum number
    of consecutive 1's in Num's binary representation.

    * to convert in binary, we use {0:b}.format() methods:    
    >>> "bin: {0:b}".format(5)
    'bin: 101'

    * then transform in to list without "0" and count all "1" between "0":
    #5(10) = 101(2)
    >>> list(map(len, "{0:b}".format(5).split("0"))) 
    '[1,1]'
    #125(10) = 1111101(2)
    >>> list(map(len, "{0:b}".format(125).split("0"))) 
    '[5,1]'

    * for print maximum number of consecutive 1's, most interesting ideas -
    use 'sorted' method, and after reverse (reverse=True) this
    new (sorted) list, get the first element in list [0].
    This will be max value:
    #125(10) = 1111101(2)
    >>> sorted(list(map(len, '{0:b}'.format(125).split("0"))), reversed=True)[0]
    '5'
"""

if __name__ == '__main__':
    Num = int(input().strip())
    print(sorted(list(map(len,
                 '{0:b}'.format(Num).split("0"))),
                 reverse=True)[0])
