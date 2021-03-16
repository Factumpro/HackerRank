''''
sWAP cASE

  https://www.hackerrank.com/challenges/swap-case/problem

  https://www.tutorialspoint.com/python/python_strings.htm
  .swapcase()
''''

''''
Sample Input 0
  s = 'HackerRank.com presents "Pythonist 2".'

Sample Output 0
  _s = hACKERrANK.COM PRESENTS "pYTHONIST 2".
''''
def swap_case(s):
    # return s.swapcase()
    _s = ""
    for i in range(len(s)):
        if s[i].islower():
            _s+=s[i].upper()
            #print(a[i].upper())
        else:
            _s+=s[i].lower()
            #print(a[i].lower())
    return _s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
