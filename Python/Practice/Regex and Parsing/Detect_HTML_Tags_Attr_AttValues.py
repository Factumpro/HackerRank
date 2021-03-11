''''
Detect HTML Tags, Attributes and Attribute Values

  Link to problem statement:
  https://hackerrank-challenge-pdfs.s3.amazonaws.com/9719-detect-html-tags-attributes-and-attribute-values-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1615477648&Signature=TjXh8bAkCIiboOSABMV5BOKh4KI%3D&response-content-disposition=inline%3B%20filename%3Ddetect-html-tags-attributes-and-attribute-values-English.pdf&response-content-type=application%2Fpdf

  You are given an HTML code snippet of N lines.
  Your task is to detect and print all the HTML tags, attributes and attribute values

  The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the
  attribute and the attribute value.

  The > symbol acts as a separator of attributes and attribute values.
  If an HTML tag has no attribute then simply print the name of the tag.
  Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags 
  ( <!--Comments --> ). Comments can be multiline.
  All attributes have an attribute value.
''''

''''
HTML PARSER LIB

  https://docs.python.org/3/library/html.parser.html
''''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
