#!/usr/bin/env python3

if __name__ == '__main__':
    N = int(input())
    names_phone_numbers = list(map(lambda _: input().split(), range(N)))
    phone_book = {
                  book_name: book_phone
                  for book_name, book_phone in names_phone_numbers
                  }
    while True:
        try:
            name = input()
            if name in phone_book:
                print('{}={}'.format(name, phone_book[name]))
            else:
                print('Not found')
        except:
            break
