def student_info():
    print("Student Details")

# faculty/details.py
def faculty_info():
    print("Faculty Details")

# main.py
from module import student_info
from faculty.details import faculty_info
student_info()
faculty_info()