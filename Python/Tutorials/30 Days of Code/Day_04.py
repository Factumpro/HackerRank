#!/usr/bin/env python3


class Person:
    def __init__(self, initialAge):
        self.age = initialAge
        if self.age < 0:
            self.age = 0
            print('Age is not valid, setting age to 0.')

    def amIOld(self):
        if self.age in range(13, 18):
            print('You are a teenager.')
        else:
            if self.age < 13:
                print('You are young.')
            else:
                print('You are old.')

    def yearPasses(self):
        self.age += 1
