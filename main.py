from courses_loader import courses_loader
from gpa_calculator import gpa_calculator

loader = courses_loader('courses.csv')
gpa = gpa_calculator(loader([2023, 2022]))
print("GPA is ", gpa)
