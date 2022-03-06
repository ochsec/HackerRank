#!/bin/python3
# https://www.hackerrank.com/challenges/grading

# import os
# import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    return list(map(curve, grades))

def curve(grade):
    if grade <= 37:
        return grade
    int_part = grade // 5
    ceil = (int_part + 1) * 5
    if ceil - grade >= 3:
        return grade
    return ceil

    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
