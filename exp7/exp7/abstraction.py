# =====================================================
# ABSTRACTION PROGRAMS (1 - 10)
# =====================================================

from abc import ABC, abstractmethod


# =====================================================
# 1. Shape Abstraction
# =====================================================
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# =====================================================
# 2. Vehicle Abstraction
# =====================================================
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike Started")

    def stop(self):
        print("Bike Stopped")


class Bus(Vehicle):
    def start(self):
        print("Bus Started")

    def stop(self):
        print("Bus Stopped")


# =====================================================
# 3. Bank Account Abstraction
# =====================================================
class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# =====================================================
# 4. Food Order Abstraction
# =====================================================
class FoodOrder(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def calculate_bill(self):
        return self.amount

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def calculate_bill(self):
        return self.amount

    def delivery_charge(self):
        return 50


# =====================================================
# 5. Patient Abstraction
# =====================================================
class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-Patient Treatment")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-Patient Treatment")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("Emergency Treatment")


# =====================================================
# 6. Transport Abstraction
# =====================================================
class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class BusTransport(Transport):
    def calculate_fare(self, distance):
        return distance * 5


class TrainTransport(Transport):
    def calculate_fare(self, distance):
        return distance * 3


class TaxiTransport(Transport):
    def calculate_fare(self, distance):
        return distance * 15


class FlightTransport(Transport):
    def calculate_fare(self, distance):
        return distance * 50


# =====================================================
# 7. Question Abstraction
# =====================================================
class Question(ABC):

    @abstractmethod
    def evaluate_answer(self):
        pass


class MCQQuestion(Question):
    def evaluate_answer(self):
        print("MCQ Answer Evaluated")


class TrueFalseQuestion(Question):
    def evaluate_answer(self):
        print("True/False Answer Evaluated")


class DescriptiveQuestion(Question):
    def evaluate_answer(self):
        print("Descriptive Answer Evaluated")


# =====================================================
# 8. Authentication Abstraction
# =====================================================
class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


# =====================================================
# 9. Cloud Storage Abstraction
# =====================================================
class CloudStorage(ABC):

    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File Uploaded to Google Drive")

    def download_file(self):
        print("File Downloaded from Google Drive")

    def delete_file(self):
        print("File Deleted from Google Drive")


class Dropbox(CloudStorage):
    def upload_file(self):
        print("File Uploaded to Dropbox")

    def download_file(self):
        print("File Downloaded from Dropbox")

    def delete_file(self):
        print("File Deleted from Dropbox")


class OneDrive(CloudStorage):
    def upload_file(self):
        print("File Uploaded to OneDrive")

    def download_file(self):
        print("File Downloaded from OneDrive")

    def delete_file(self):
        print("File Deleted from OneDrive")


# =====================================================
# 10. Appointment Abstraction
# =====================================================
class Appointment(ABC):

    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General Appointment Booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist Appointment Booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency Appointment Booked")

    def calculate_fee(self):
        return 2000


# =====================================================
# SAMPLE TESTING
# =====================================================
if __name__ == "__main__":

    shapes = [Circle(5), Rectangle(4, 6), Triangle(4, 8)]
    for s in shapes:
        print("Area:", s.area())

    vehicles = [Car(), Bike(), Bus()]
    for v in vehicles:
        v.start()
        v.stop()

    auth_methods = [
        PasswordAuthentication(),
        OTPAuthentication(),
        BiometricAuthentication()
    ]
    for auth in auth_methods:
        auth.authenticate()

    storage = GoogleDrive()
    storage.upload_file()
    storage.download_file()
    storage.delete_file()

    appointment = SpecialistAppointment()
    appointment.book_appointment()
    print("Fee:", appointment.calculate_fee())