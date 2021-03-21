'''
String Formatting

  https://www.hackerrank.com/challenges/python-string-formatting/problem
'''

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range (1,number+1):
        print (str(i).rjust(width,' '),str(oct(i)[2:]).rjust(width,' '),str(hex(i)[2:].upper()).rjust(width,' '),str(bin(i)[2:]).rjust(width,' '),sep=' ')