'''
Find a string

  https://www.hackerrank.com/challenges/find-a-string/problem
'''

def count_substring(string, sub_string):
  _count = 0
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            _count +=1
    return _count
  '''
    _count = 1
    _count = sum([_count for i in range(0, len(string)) if string[i:i+len(sub_string)] == sub_string]) 
    return _count 
  '''

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)