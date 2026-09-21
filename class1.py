# =========================
# 1. Student
# =========================
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}, Percentage: {self.percentage():.2f}%")

        


# =========================
# 2. Employee
# =========================
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def hra(self):
        return self.basic_salary * 0.20

    def da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.hra() + self.da()


# =========================
# 3. Rectangle
# =========================
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# =========================
# 4. Circle
# =========================
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# =========================
# 5. Book
# =========================
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"ID:{self.book_id}, Title:{self.title}, Author:{self.author}, Price:{self.price}")


# =========================
# 6. Electricity Bill
# =========================
class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            return self.units * 1.5
        elif self.units <= 300:
            return 100 * 1.5 + (self.units - 100) * 2.5
        else:
            return 100 * 1.5 + 200 * 2.5 + (self.units - 300) * 4


# =========================
# 7. Mobile Phone
# =========================
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print(f"{self.brand} {self.model}, Storage: {self.storage}, Price: {self.price}")

    def discounted_price(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


# =========================
# 8. Patient
# =========================
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print(f"ID:{self.patient_id}, Name:{self.name}, Age:{self.age}, Disease:{self.disease}")

    def total_bill(self):
        return self.consultation_fee


# =========================
# 9. ATM
# =========================
class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_details(self):
        print(f"Account No: {self.account_no}, Name: {self.name}, Balance: {self.balance}")


# =========================
# 10. Vehicle Rental
# =========================
class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle Rented")
        else:
            print("Not Available")

    def return_vehicle(self):
        self.available = True
        print("Vehicle Returned")

    def rental_charge(self, days):
        return self.rental_rate * days


# =========================
# 11. Shopping Cart
# =========================
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append((name, price))

    def remove_product(self, name):
        self.products = [p for p in self.products if p[0] != name]

    def total_bill(self):
        return sum(price for _, price in self.products)

    def __del__(self):
        print("Shopping Cart Destroyed")


# =========================
# 12. Food Order
# =========================
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        return self.quantity * self.price

    def __del__(self):
        print("Order Completed")


# =========================
# 13. Student Result
# =========================
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        p = self.percentage()

        if p >= 75:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 40:
            return "C"
        else:
            return "F"

    def __del__(self):
        print("Student Result Object Destroyed")


# =========================
# Sample Testing
# =========================
if __name__ == "__main__":

    s = Student(1, "Bhavya", [80, 90, 85])
    s.display()

    e = Employee(101, "Aman", 30000)
    print("Gross Salary:", e.gross_salary())

    r = Rectangle(10, 5)
    print("Area:", r.area(), "Perimeter:", r.perimeter())

    c = Circle(7)
    print("Circle Area:", c.area())

    b = Book(1, "Python", "Guido", 500)
    b.display()

    eb = ElectricityBill(1001, "Rahul", 350)
    print("Bill:", eb.calculate_bill())

    m = MobilePhone("Apple", "iPhone", "128GB", 70000)
    print("Discounted Price:", m.discounted_price(10))

    p = Patient(1, "Riya", 20, "Fever", 500)
    print("Total Bill:", p.total_bill())

    atm = ATM(12345, "Bhavya", 10000)
    atm.deposit(2000)
    atm.withdraw(1500)
    atm.check_balance()

    v = Vehicle("MH09AB1234", "Swift", 1000)
    print("Rental Charge:", v.rental_charge(5))

    cart = ShoppingCart("Bhavya", 1)
    cart.add_product("Laptop", 50000)
    cart.add_product("Mouse", 500)
    print("Cart Total:", cart.total_bill())

    order = FoodOrder(1, "Bhavya", "Pizza", 2, 250)
    print("Food Bill:", order.total_bill())

    result = StudentResult("Bhavya", [80, 90, 85, 75, 95])
    print("Percentage:", result.percentage())
    print("Grade:", result.grade())