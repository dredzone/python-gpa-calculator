import csv
from collections import namedtuple


def courses_loader(file: str):
    field_types = [int, str, str, str, str]
    courses = list()
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile)
        Course = namedtuple("Course", next(reader))
        for row in reader:
            row = tuple(convert(value) for convert, value in zip(field_types, row))
            courses.append(Course(*row))

    courses = sorted(courses, key=lambda course: course.year, reverse=True)

    def loader(years=()):
        if len(years) == 0:
            return courses.copy()

        filtered = list()
        for course in courses:
            if course.year in years:
                filtered.append(course)
        return filtered

    return loader


