#!/usr/bin/env python3

import math


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisor_sum(self, n):
        div_sum_ = 0
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0:
                if n / i == i:
                    div_sum_ += i
                else:
                    div_sum_ += i + n/i
            i += 1
        return int(div_sum_)

if __name__ == '__main__':
    n = int(input())
    my_calc = Calculator()
    s = my_calc.divisorSum(n)
    print("I implemented: ", type(my_calc).__bases__[0].__name__)
    print(s)
