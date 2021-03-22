'''
Set .add()

  https://www.hackerrank.com/challenges/py-set-add/problem

'''

'''
If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    arr=set([])
    for _ in range (n):
        
        arr.add(input())
        
    print(len(arr))