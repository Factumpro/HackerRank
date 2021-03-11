''''
Validating UID 

  ABCXYZ company has up to 100 employees.
  The company decides to create a unique identification number (UID) for each of its employees.
  The company has assigned you the task of validating all the randomly generated UIDs.

  A valid UID must follow the rules below:

  It must contain at least 2 uppercase English alphabet characters.
  It must contain at least 3 digits (0-9).
  It should only contain alphanumeric characters (a-z,A-Z & 0-9).
  No character should repeat.
  There must be exactly 10 characters in a valid UID.
''''

''''
EXPLANATION
  r^(?=(?:[a-z\d][A-Z]){2})(?=(?:\D\d){3})(?:([a-zA-Z\d])(?!.\1)){10}$

  ^ asserts position at start of a line

  Positive Lookahead (?=(?:[a-z\d][A-Z]){2})
    Assert that the Regex below matches

      Non-capturing group (?:[a-z\d][A-Z]){2}
      {2} matches the previous token exactly 2 times

      Match a single character present in the list below [a-z\d]
        * matches the previous token between zero and unlimited times, 
          as many times as possible, giving back as needed (greedy)
        a-z matches a single character in the range between a (index 97) 
          and z (index 122) (case sensitive)
        \d matches a digit (equivalent to [0-9])

      Match a single character present in the list below [A-Z]
        A-Z matches a single character in the range between A (index 65) 
        and Z (index 90) (case sensitive)

  Positive Lookahead (?=(?:\D\d){3})
    Assert that the Regex below matches

      Non-capturing group (?:\D\d){3}
      {3} matches the previous token exactly 3 times

      \D matches any character that's not a digit (equivalent to [^0-9])
        * matches the previous token between zero and unlimited times, 
          as many times as possible, giving back as needed (greedy)
      \d matches a digit (equivalent to [0-9])

  Non-capturing group (?:([a-zA-Z\d])(?!.\1)){10}
    {10} matches the previous token exactly 10 times

    1st Capturing Group ([a-zA-Z\d])
      Match a single character present in the list below [a-zA-Z\d]

      a-z matches a single character in the range between a (index 97) 
          and z (index 122) (case sensitive)
      A-Z matches a single character in the range between A (index 65) 
          and Z (index 90) (case sensitive)
      \d matches a digit (equivalent to [0-9])
    
    Negative Lookahead (?!.\1)
      Assert that the Regex below does not match

      . matches any character (except for line terminators)
      \1 matches the same text as most recently matched by the 1st capturing group

  $ asserts position at the end of a line

  Global pattern flags
  g modifier: global. All matches (don't return after first match)
  m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
''''

''''
  RegEx Learn, Build, & Test:
      https://regex101.com/
  Read More:
    https://www.regular-expressions.info/lookaround.html
    https://www.tutorialspoint.com/python/python_reg_expressions.htm
''''

'''' 
TEST 
    pattern = r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$'
    reg = re.compile(pattern)
    arr = ['A1b2c3d4eF', 'B1CDEF2354', 'AB123CDEF5', 'B1CD102354', 'a1bcf2coqb', 'a1bcf2oo3b', '1234567890ABC']
    for i in arr:
        print(i, reg.match(i)) 
''''

import re

pattern = r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$'

for x in range(int(input())):
    
    if re.match(pattern,str(input())):
        print("Valid")
    else:
        print("Invalid")
