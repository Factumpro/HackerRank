'''
Designer Door Mat
  https://www.hackerrank.com/challenges/designer-door-mat/problem
'''

#!/usr/bin/python3
x, y = map(int,input().split())
print ("\n".join([(".|."*(2*i +1)).center(y, "-") for i in range (x//2)]) +
"\n" +("WELCOME".center(3*x,"-")) + "\n" +
"\n".join([(".|."*(i)).center(y, "-") for i in range (x -2,-1,-2)]))