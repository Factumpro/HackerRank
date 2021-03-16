'''
Mutations 

  https://www.hackerrank.com/challenges/python-mutations/problem

  We have seen that lists are mutable (they can be changed), 
  and tuples are immutable (they cannot be changed).
'''

def mutate_string(string, position, character):
    _str_2_list = list(string)    
    _str_2_list[position] = character
    return ''.join(_str_2_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)