#!/usr/bin/env python3

def gradingStudents(grades):
    final_grade = []
    for origin in grades:
        difference = 5 - origin%5
        if origin >= 38 and difference < 3:
            origin += difference
        final_grade.append(origin)
    return final_grade

