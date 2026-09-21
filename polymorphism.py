# =====================================================
# POLYMORPHISM PROGRAMS (1 - 15)
# =====================================================

# =====================================================
# 1. Shape - Runtime Polymorphism
# =====================================================
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h


# =====================================================
# 2. Employee Salary Polymorphism
# =====================================================
class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 10000

class Developer(Employee):
    def calculate_salary(self):
        return 50000 + 7000

class Tester(Employee):
    def calculate_salary(self):
        return 50000 + 5000


# =====================================================
# 3. Vehicle Start
# =====================================================
class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with ignition")


# =====================================================
# 4. Animal Sound
# =====================================================
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")

class Lion(Animal):
    def sound(self):
        print("Roar")


# =====================================================
# 5. Notification
# =====================================================
class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


# =====================================================
# 6. Student Grade
# =====================================================
class Student:
    def calculate_grade(self, marks):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 75 else "B"

class MedicalStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 80 else "B"

class ManagementStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 70 else "B"


# =====================================================
# 7. Bank Interest
# =====================================================
class BankAccount:
    def calculate_interest(self, amount):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        return amount * 0.05

class CurrentAccount(BankAccount):
    def calculate_interest(self, amount):
        return amount * 0.02

class FixedDepositAccount(BankAccount):
    def calculate_interest(self, amount):
        return amount * 0.08


# =====================================================
# 8. Report Generation
# =====================================================
class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")

class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")

def create_report(report):
    report.generate()


# =====================================================
# 9. Operator Overloading (+)
# =====================================================
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches

        feet += inches // 12
        inches %= 12

        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


# =====================================================
# 10. Student Comparison
# =====================================================
class StudentCompare:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


# =====================================================
# 11. Product Comparison
# =====================================================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


# =====================================================
# 12. Payment Module
# =====================================================
class Payment:
    def make_payment(self, amount):
        pass

class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI Payment:", amount)

class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card Payment:", amount)

class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet Payment:", amount)

def process_payment(payment, amount):
    payment.make_payment(amount)


# =====================================================
# 13. Person Roles
# =====================================================
class Person:
    def display_role(self):
        pass

class Student(Person):
    def display_role(self):
        print("Student")

class Faculty(Person):
    def display_role(self):
        print("Faculty")

class Administrator(Person):
    def display_role(self):
        print("Administrator")


# =====================================================
# 14. Media Player
# =====================================================
class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        print("Playing Audio")

class Video(Media):
    def play(self):
        print("Playing Video")

class Podcast(Media):
    def play(self):
        print("Playing Podcast")


# =====================================================
# 15. Smart Devices
# =====================================================
class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        print("Light ON")

    def turn_off(self):
        print("Light OFF")

class Fan(SmartDevice):
    def turn_on(self):
        print("Fan ON")

    def turn_off(self):
        print("Fan OFF")

class AC(SmartDevice):
    def turn_on(self):
        print("AC ON")

    def turn_off(self):
        print("AC OFF")

class TV(SmartDevice):
    def turn_on(self):
        print("TV ON")

    def turn_off(self):
        print("TV OFF")


# =====================================================
# SAMPLE TESTING
# =====================================================
if __name__ == "__main__":

    shapes = [Circle(5), Rectangle(4, 6), Triangle(4, 8)]
    for s in shapes:
        print("Area:", s.area())

    employees = [Manager(), Developer(), Tester()]
    for e in employees:
        print("Salary:", e.calculate_salary())

    vehicles = [Car(), Bike(), Bus()]
    for v in vehicles:
        v.start()

    animals = [Dog(), Cat(), Cow(), Lion()]
    for a in animals:
        a.sound()

    notifications = [
        EmailNotification(),
        SMSNotification(),
        PushNotification()
    ]
    for n in notifications:
        n.send()

    create_report(PDFReport())
    create_report(ExcelReport())
    create_report(HTMLReport())

    d1 = Distance(5, 10)
    d2 = Distance(3, 8)
    d3 = d1 + d2
    d3.display()

    p1 = Product("Laptop", 50000)
    p2 = Product("Mobile", 40000)
    print(p1 > p2)

    process_payment(UPIPayment(), 1000)

    persons = [Student(), Faculty(), Administrator()]
    for p in persons:
        p.display_role()

    media = [Audio(), Video(), Podcast()]
    for m in media:
        m.play()

    devices = [Light(), Fan(), AC(), TV()]
    for d in devices:
        d.turn_on()
        d.turn_off()