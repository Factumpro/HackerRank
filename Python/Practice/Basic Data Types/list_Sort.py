''''
Find the Runner-Up Score!

  Link to problem statement:
  https://hackerrank-challenge-pdfs.s3.amazonaws.com/1374-find-second-maximum-number-in-a-list-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1615488044&Signature=ZdTn2jJUPO4GpBf6oBIjSDfeAbE%3D&response-content-disposition=inline%3B%20filename%3Dfind-second-maximum-number-in-a-list-English.pdf&response-content-type=application%2Fpdf

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
