'''
Set .discard(), .remove() & .pop()

  https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

'''

'''


'''

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd = input().split()   
    if len(cmd) == 1: eval('s.'+cmd[0])() 
    if len(cmd) == 2: eval('s.'+cmd[0])(int(cmd[1]))
print(sum(s))
