'''
Basic Data Types\Tuples

  https://www.hackerrank.com/challenges/python-tuples/problem

  https://www.w3schools.com/python/python_tuples.asp
  
'''

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tulp = tuple(integer_list)
    
    print( hash(tulp) )