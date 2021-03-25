'''
Day 25: Running Time and Complexity
  https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

  https://www.bigprimes.net/primalitytest

'''

'''
#Im try to understand , if we use BINARY code for prime algorithm 
#it will by work in Q(sqrt(n)) or not (im not finished this code)

from math import sqrt

def bin__startTrue(int_num):
  return bool(int_num & (0b1<<0))

#PRIME LIST FOR TEST
check_list = [
 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
 191, 193, 197, 2796203, 5419, 1133836730401, 15790321,
 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
 467, 479, 487, 491, 499, 503, 509, 521, 523, 541 
 ]

# NOT PRIME LIST
check_list = [510,511,512,513,514,515,516,517,518,519,520,42,44,45,46,54,55,56,
57,66,69,70,82,81,102,105,111,5420,5204,5205,1735,348,174,172, 15790323]


bool_prime = False
for num in check_list:
  if bin__startTrue(num):
    n =int((num - (1*sqrt(num)))/(8*sqrt(num)))
    if n == 0 or n == 1: n = 2

    for i in range(1,n+1):
        if (num/(8*i-1)).is_integer(): 
          bool_prime = False
          print('Not Prime')
          break
        elif (num/(8*i+1)).is_integer(): 
          bool_prime = False
          print('Not Prime') 
          break
        elif (num/(8*i-3)).is_integer(): 
          bool_prime = False
          print('Not Prime') 
          break
        elif (num/(8*i+3)).is_integer(): 
          bool_prime = False
          print('Not Prime') 
          break
        else:
          bool_prime = True
          continue

    if bool_prime: 
      print('prime {}'.format(num)) 
  else:
    print('Not Prime')
'''

# Q(sqrt(n))
from math import sqrt

N = int(input())
for _ in range(N):
    num = int(input())
    if(num == 1):
        print("Not prime")
    else:
        if(num % 2 == 0 and num > 2):
            print("Not prime")
        else:
            for i in range(3, int(sqrt(num))+1, 2):
                if num % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")