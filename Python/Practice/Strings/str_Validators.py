'''
String Validators

  https://www.hackerrank.com/challenges/string-validators/problem
'''

if __name__ == '__main__':
    string = input()
    #string = 'sQ2' #all true
    '''
    print(any(_.isalnum() for _ in string))
    print(any(_.isalpha() for _ in string))
    print(any(_.isdigit() for _ in string))
    print(any(_.islower() for _ in string))
    print(any(_.isupper() for _ in string))
    '''  
    print("\n".join(str(any(bool_item)) for bool_item in list(zip(*[[        
        string_is.isalnum(),
        string_is.isalpha(),
        string_is.isdigit(),
        string_is.islower(),
        string_is.isupper()
    ] for string_is in string]))))