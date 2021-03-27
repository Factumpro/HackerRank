#!/usr/bin/env python3

from abc import ABCMeta


class Book(metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass


class MyBook(Book):
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    @classmethod
    def display(self):
        print ('Title: {}\nAuthor: {}\nPrice: {}'
               .format(title, author, price))

if __name__ == '__main__':
    title = input()
    author = input()
    price = int(input())
    new_novel = MyBook(title, author, price)
    new_novel.display()
