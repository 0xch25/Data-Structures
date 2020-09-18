'''
https://www.hackerrank.com/challenges/grading/problem?isFullScreen=false
'''


def gradingStudents(grades):
    for i in range(len(grades)):
        if (grades[i] > 37):
            if ((grades[i] % 5) != 0):
                if (5 - (grades[i] % 5) < 3):
                    grades[i] += 5 - (grades[i] % 5)
    return (grades)
grades=[36,40,53,52]
print(gradingStudents(grades))
