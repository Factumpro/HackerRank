''''
HTML Parser - Part 2

  Link to problem statement:
  https://hackerrank-challenge-pdfs.s3.amazonaws.com/11665-html-parser-part-2-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1615479172&Signature=9TacYkxu4IzevkmgdoBYio1QpzI%3D&response-content-disposition=inline%3B%20filename%3Dhtml-parser-part-2-English.pdf&response-content-type=application%2Fpdf

  Task:
  You are given an HTML code snippet of N lines.
  Your task is to print the single-line comments, multi-line comments and the data.

  Note: Do not print data if data == '\n' .

  Print the single-line comments, multi-line comments and the data in order of 
  their occurrence from top to bottom in the snippet.
  Format the answers as explained in the problem statement.
''''

''''
HTML PARSER LIB

  https://docs.python.org/3/library/html.parser.html
''''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment  ", data, sep="\n")
        else:
            print(">>> Single-line Comment  ", data, sep="\n")
            
    def handle_data(self, data):
        if data != "\n":
            print(">>> Data", data, sep="\n") 
  

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
