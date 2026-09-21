# =====================================================
# 1. Employee -> Manager
# =====================================================
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        print(self.emp_id, self.name, self.salary, self.department)
        print("Annual Salary:", self.annual_salary())


# =====================================================
# 2. Vehicle -> Car
# =====================================================
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


# =====================================================
# 3. Academic + Sports -> Student
# =====================================================
class Academic:
    def __init__(self, marks):
        self.marks = marks

class Sports:
    def __init__(self, points):
        self.points = points

class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        return self.marks + self.points


# =====================================================
# 4. PersonalDetails + ProfessionalDetails -> EmployeeInfo
# =====================================================
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

class EmployeeInfo(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print(self.name, self.age, self.emp_id,
              self.designation, self.salary)


# =====================================================
# 5. Person -> Student -> ResearchStudent
# =====================================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course,
                 topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide


# =====================================================
# 6. BankAccount -> SavingsAccount -> PremiumSavingsAccount
# =====================================================
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, rate):
        super().__init__(acc_no, balance)
        self.rate = rate

    def calculate_interest(self):
        return self.balance * self.rate / 100

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, acc_no, balance, rate, benefit):
        super().__init__(acc_no, balance, rate)
        self.benefit = benefit


# =====================================================
# 7. Shape Hierarchy
# =====================================================
class Shape:
    def display_name(self):
        print("Shape")

class Circle(Shape):
    def area(self, r):
        return 3.14 * r * r

class Rectangle(Shape):
    def area(self, l, b):
        return l * b

class Triangle(Shape):
    def area(self, b, h):
        return 0.5 * b * h


# =====================================================
# 8. Employee -> Manager, Developer, Tester
# =====================================================
class Employee:
    def __init__(self, emp_id, name, basic):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic

class Manager(Employee):
    def salary(self):
        return self.basic + 10000

class Developer(Employee):
    def salary(self):
        return self.basic + 7000

class Tester(Employee):
    def salary(self):
        return self.basic + 5000


# =====================================================
# 9. Person -> Student, Faculty -> TeachingAssistant
# =====================================================
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

class Faculty(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class TeachingAssistant(Student, Faculty):
    def __init__(self, name, roll, subject):
        Student.__init__(self, name, roll)
        self.subject = subject


# =====================================================
# 10. Vehicle -> Car -> SportsCar
#     Vehicle -> Bike -> ElectricBike
# =====================================================
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

class Bike(Vehicle):
    def __init__(self, brand, mileage):
        super().__init__(brand)
        self.mileage = mileage

class ElectricBike(Bike):
    def __init__(self, brand, mileage, battery):
        super().__init__(brand, mileage)
        self.battery = battery


# =====================================================
# 11. Student -> Result
# =====================================================
class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

class Result(Student):
    def __init__(self, roll_no, name, course,
                 m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def percentage(self):
        return self.total() / 3


# =====================================================
# 12. Product -> ElectronicProduct
# =====================================================
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, pid, name, price,
                 brand, warranty):
        super().__init__(pid, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - self.price * discount / 100


# =====================================================
# 13. Printer + Scanner -> MultifunctionDevice
# =====================================================
class Printer:
    def print_doc(self):
        print("Printing Document")

class Scanner:
    def scan_doc(self):
        print("Scanning Document")

class MultifunctionDevice(Printer, Scanner):
    pass


# =====================================================
# 14. Camera + Phone -> Smartphone
# =====================================================
class Camera:
    def take_photo(self):
        print("Photo Captured")

class Phone:
    def make_call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    pass


# =====================================================
# 15. Person -> Student -> ResearchStudent
# =====================================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll, course):
        super().__init__(name, age)
        self.roll = roll
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll,
                 course, topic, guide):
        super().__init__(name, age, roll, course)
        self.topic = topic
        self.guide = guide


# =====================================================
# 16. Same as Program 15
# =====================================================
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student2(Person2):
    def __init__(self, name, age, roll, course):
        super().__init__(name, age)
        self.roll = roll
        self.course = course

class ResearchStudent2(Student2):
    def __init__(self, name, age, roll,
                 course, topic, guide):
        super().__init__(name, age, roll, course)
        self.topic = topic
        self.guide = guide


# =====================================================
# 17. Animal Hierarchy
# =====================================================
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")


# =====================================================
# 18. Person -> Doctor, Patient
#     Doctor -> Surgeon, MedicalResearcher
# =====================================================
class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def treat(self):
        print("Treating Patient")

class Patient(Person):
    def receive_treatment(self):
        print("Receiving Treatment")

class Surgeon(Doctor):
    def surgery(self):
        print("Performing Surgery")

class MedicalResearcher(Doctor):
    def research(self):
        print("Conducting Research")