#!/usr/bin/env python3
"""
a python function that returns all students sorted by average scores
"""


def top_students(mongo_collection):
    """
    returns all studets sorted by average scores
    """
    students = mongo_collection.find()
    students_avg_grade = {}

    for student in students:
        total = 0
        for topic in student["topics"]:
            total += topic["score"]

        average = total / len(student["topics"])
        students_avg_grade[average] = student

    sorted_list = sorted([key for key in students_avg_grade.keys()],
                         reverse=True)

    newStudentList = []
    for average in sorted_list:
        students_avg_grade[average]["averageScore"] = average
        newStudentList.append(students_avg_grade[average])

    return newStudentList
