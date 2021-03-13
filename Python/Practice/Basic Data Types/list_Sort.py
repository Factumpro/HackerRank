''''
Find the Runner-Up Score!

  Link to problem statement:
  https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

''''

''''
Sort with loop 

  if __name__ == '__main__':
      n = int(input())
      arr = list(map(int, input().split()))
      
      a = arr[0]
      for i in range(n):
          if arr[i] != max(arr) and arr[i] > a :
              a = arr[i]
      print (a)
''''

if __name__ == '__main__':

    N=int(input())
    list=list(set(map(int,input().strip().split(" "))))
    list.sort(reverse=True) # [ max, ... , min] -> 0, ... , n
    print ( list[1] ) # 1 - runner-up score index
