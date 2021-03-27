#!/usr/bin/env python3


class Person:
	"""Abstract class
	!!! Need documentation written.
	"""
	
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def print_person(self):
        print("Name: {last_name}, {first_name}"
              .format(first_name=self.first_name,
                      last_name=self.last_name))
        print("ID:", self.id_number)


class Student(Person):
    """Class Constructor(Inheritance)
    :first_name - A string denoting the Person's first name.
    :last_name - A string denoting the Person's last name.
    :id_number - An integer denoting the Person's ID number.
    :scores - An array of integers denoting the Person's test scores.
    Write your constructor here
    """

    def __init__(self, first_name, last_name, id_number, scores):
        super().__init__(first_name, last_name, id_number)
        self.scores = scores
        self.scores_ = []

    def calculate(self):
        self.scores_ = self.scores
        average_ = sum(self.scores_)/len(self.scores_)
        if average_ >= 70:
            if average_ < 80:
                return "A"
            else:
                if average_ < 90:
                    return "E"
                else:
                    return "O"
        else:
            if average_ < 40:
                return "T"
            else:
                if average_ < 55:
                    return "D"
                else:
                    return "P"

"""
####TEST
    listScore = [ [90,90], [80,80], [70,70], [55,55],[40,40],[35,35] ]
    for i in listScore:
      firstName = 'firstName'
      lastName = 'lastName'
      idNum = '8135627'
      scores = i
      s = Student(first_name, last_name, id_number, scores)
      s.printPerson()
      print("Grade:", s.calculate())
"""

if __name__ == '__main__':
    first_name,
    last_name,
    id_number = input().split()
    _ = int(input())
    scores = list(map(int, input().split()))
    s = Student(first_name, last_name, id_number, scores)
    s.print_person()
    print("Grade:", s.calculate())
