#!/usr/bin/env python3

from operator import itemgetter

INDEX_NAME = 0
INDEX_SCORE = 1


def minScore(students):
    min_score = min(students, key=itemgetter(INDEX_SCORE))
    min_score_list = []
    [min_score_list.append(i) for i in students
     if i[INDEX_SCORE] == min_score[INDEX_SCORE]]
    return min_score_list

if __name__ == '__main__':
    N = int(input())
    students = list(map(lambda _: [input(), float(input())], range(N)))
    students.sort(key=itemgetter(INDEX_SCORE, INDEX_NAME))
    min_score = minScore(students)
    [students.remove(i) for i in min_score]
    min_score = minScore(students)
    [print(students[INDEX_NAME]) for students in min_score]
