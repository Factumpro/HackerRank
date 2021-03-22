'''
Set Mutations

  https://www.hackerrank.com/challenges/py-set-mutations/problem

set(map(int, input().split())) 
cmd
eval
sum
'''

'''
Sample Input
  16
  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
  4
  intersection_update 10
  2 3 5 6 8 9 1 4 7 11
  update 2
  55 66
  symmetric_difference_update 5
  22 7 35 62 58
  difference_update 7
  11 22 35 55 58 62 66

Sample Output
  38

 '''

length, x1 = input(), set(map(int, input().split())) 
for _ in range(int(input())):
    cmd = input().split()
    eval("x1. "+cmd[0])(*[map(int, input().split())])
print(sum(x1))
