class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    _scores = []

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self._scores = scores

    '''
    def printScore(self):
        print("scores:", self._scores)
    '''

    def calculate(self):
        __average = sum(self._scores)/len(self._scores)
        if __average >= 70:
          if __average < 80:
            return "A"
          else: 
            if __average < 90:
              return "E"
            else:
              return "O"
        else:
          if __average < 40:
            return "T"
          else: 
            if __average < 55:
              return "D"
            else:
              return "P"
        
        #print(_sum)       

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

'''
#TEST

listScore = [ [90,90], [80,80], [70,70], [55,55],[40,40],[35,35] ]
for i in listScore:

  firstName = 'firstName'
  lastName = 'lastName'
  idNum = '8135627'
  scores = i
  s = Student(firstName, lastName, idNum, scores)
  s.printPerson()
  print("Grade:", s.calculate())
'''

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())