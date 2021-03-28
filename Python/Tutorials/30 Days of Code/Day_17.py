#!/usr/bin/env python3

"""
    More Exceptions (PEP 352)
    ---------------

    https://docs.python.org/3/tutorial/errors.html (8.6.User-defined Exception)
    https://www.programiz.com/python-programming/user-defined-exception
"""


class Exception(BaseException):
    pass


class Calculator:
    def __init__(self):
        pass

    def power(self, n, p):
        if (n < 0 or
                p < 0):
            raise Exception('n and p should be non-negative')
        else:
            return (n**p)

if __name__ == '__main__':
    my_calc = Calculator()
    for _ in range(int(input())):
        n, p = map(int, input().split())
        try:
            ans = my_calc.power(n, p)
            print(ans)
        except Exception as e:
            print(e)
