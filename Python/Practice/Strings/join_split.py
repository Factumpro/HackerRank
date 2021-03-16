'''
String Split and Join

  https://www.hackerrank.com/challenges/python-string-split-and-join/problem


  string = 'join'.join(string)
  string = string.split('split_element')
'''

'''
Sample Input
  this is a string   

Sample Output
  this-is-a-string
'''

def split_and_join(line):
    _list = line
    _list = _list.split(" ") # delimiter
    '''
    when you use join without split, your str output will by
      t-h-i-s- -i-s- -a- -s-t-r-i-n-g
    '''
    _list = "-".join(_list)
    #return print(type(_list)) str
    #return print(_list)
    # write your code here
    return _list

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)