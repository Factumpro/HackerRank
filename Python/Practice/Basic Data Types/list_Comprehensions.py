''''
List Comprehensions

  Link to problem statement:
  https://hackerrank-challenge-pdfs.s3.amazonaws.com/1572-list-comprehensions-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1615487524&Signature=v7JQP%2BvDq%2BTBvhRZjCKjPSV%2Fsq4%3D&response-content-disposition=inline%3B%20filename%3Dlist-comprehensions-English.pdf&response-content-type=application%2Fpdf


''''

''''
Tutorial
  https://www.hackerrank.com/challenges/list-comprehensions/tutorial

The simplest form of a list comprehension is:
  [ expression-involving-loop-variable for loop-variable in sequence ]

List comprehensions can be nested where they take the following form:
  [ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]

The final form of list comprehension involves creating a list and filtering it similar to using the filter() method. The filtering form of list comprehension takes the following form:
  [ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]
''''

''''
Sample Input 1
  1
  1
  1
  2
Sample Output 1
  [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
''''

if __name__ == '__main__':

  x, y, z, n = (int(input()) for _ in range(4))

  print ([ [a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) 
  if a + b + c != n ])
