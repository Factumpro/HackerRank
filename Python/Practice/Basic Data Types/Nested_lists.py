''''
Nested Lists

  Link to problem statement:
  https://www.hackerrank.com/challenges/nested-list/problem

  Given the names and grades for each student in a class of N students, 
  store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

  Note: If there are multiple students with the second lowest grade, order 
  their names alphabetically and print each name on a new line.

  Sample Input 0
    
    5    
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39

  Sample Output 0

    Berry
    Harry

''''

from operator import itemgetter

if __name__ == '__main__':
    
    N = int(input())
    students_list = list(map(lambda _: [input(),float(input())], range(N)))
        
    min_score_list = []
    
    students_list.sort(key =itemgetter(1,0))
    min_score = min(students_list, key =itemgetter(1))

    #print(list(students_list))
    #print(min_score[1])    
    
    for i in students_list:
        #print(list(i))
        if i[1] == min_score[1]:
            min_score_list.append(i)
            
    for i in min_score_list:
        students_list.remove(i)
  
    min_score = min(students_list, key =itemgetter(1))
    for i in students_list:
        #print(list(i))
        if i[1] == min_score[1]:
        #min_score_list.append(i)
            print(i[0])
