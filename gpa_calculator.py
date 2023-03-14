from grade_converter import grade_converter


def gpa_calculator(courses):
    total = float(0.0)
    for [year, course, weight, grade, instructor] in courses:
        total += grade_converter(grade, weight)
    return total / len(courses)
