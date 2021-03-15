'''
Basic Data Types\Lists

  Link to problem statement:
  https://www.hackerrank.com/challenges/python-lists/problem

  eval() Function:
    https://www.w3schools.com/python/ref_func_eval.asp

  getattr() Function:
  https://www.programiz.com/python-programming/methods/built-in/getattr

    lists=[]
    parts = ['append','remove', 'insert', 'print']
    print( list(lists))
    getattr(lists, parts[0])('add')
    print( list(lists))
    getattr(lists, 'pop')() #remove 
    print( list(lists))
'''

'''
another option:

    N = int(input())
    lists = []
    for _ in range(N):
      args = input().split()
      if args[0] == "append":
          lists.append(int(args[1]))
      elif args[0] == "insert":
          lists.insert(int(args[1]), int(args[2]))
      elif args[0] == "remove":
          lists.remove(int(args[1]))
      elif args[0] == "pop":
          lists.pop()
      elif args[0] == "sort":
          lists.sort()
      elif args[0] == "reverse":
          lists.reverse()
      elif args[0] == "print":
          print (list(lists)) 
'''
'''
if __name__ == '__main__':
    N = int(input())
    lists = []
    for _ in range(N):
        line = input().strip()
        if line == 'print':
            print (list(lists))            
        else:
            parts = line.split()
            getattr(lists, parts[0])(*(map(int, parts[1:])))
'''

if __name__ == '__main__':
    N = int(input())
    lists = []
    for _ in range(N):
        string = input().split()
        command = string[0]
        list_args = string[1:]
        
        if command !="print":
            command += "("+ ",".join(list_args) +")"            
            eval("lists." +command)
        else:
            print(list(lists))