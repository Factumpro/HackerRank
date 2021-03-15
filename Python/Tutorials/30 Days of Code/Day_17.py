'''
Day 17: More Exceptions

  8.6. User-defined Exceptions:
  https://docs.python.org/3/tutorial/errors.html
  https://www.programiz.com/python-programming/user-defined-exception

  Raised Exceptions must derive from BaseException:
  https://rules.sonarsource.com/python/RSPEC-5632

'''

'''
Sample Input

  4
  3 5
  2 4
  -1 -2
  -1 3
Sample Output

  243
  16
  n and p should be non-negative
  n and p should be non-negative
'''

'''
another option:

class AbstractException(BaseException):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class Exception(AbstractException):
    def __init__(self, message = 'n and p should be non-negative'):
        self.message = message
        super().__init__(self.message)
'''

class Exception(BaseException):
    pass

class Calculator:
    def __init__(self):
        pass
    
    def power(self,n,p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        else:
            _result = n**p
            return _result

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   