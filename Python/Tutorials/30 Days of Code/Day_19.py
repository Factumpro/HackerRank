'''
Day 19: Interfaces

'''

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

import math
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        _sumd = 0
        i = 1
        '''
        for i in range(1,n+1):
            if (n % i==0) :
                _sumd +=i
            i = i + 1
        return _sumd
        '''
        for i in range(1,int(math.sqrt(n))+1):        
            if (n % i == 0) :  
                if (n / i == i) :
                    _sumd +=i
                else :                
                    _sumd +=i + n/i
            i = i + 1
        return int(_sumd)
        
        
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)