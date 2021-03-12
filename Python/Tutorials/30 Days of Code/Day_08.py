# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

names_phone_numbers = list(map(lambda _: input().split(), range(n)))
phone_book = {book_name: book_phone for book_name,book_phone in names_phone_numbers}

while True:
    try:
        name = input()
        if name in phone_book:
            print('{}={}'.format(name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
