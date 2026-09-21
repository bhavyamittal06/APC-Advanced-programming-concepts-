def total(m1,m2,m3): return m1+m2+m3
def percentage(t): return t/3
def grade(p):
    if p>=90:return "A"
    elif p>=75:return "B"
    else:return "C"
# main.py
import student
t=student.total(80,90,85)
p=student.percentage(t)
print(student.grade(p))