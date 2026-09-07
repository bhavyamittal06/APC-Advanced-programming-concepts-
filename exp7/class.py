class Student:
    # Constructor
    def __init__(self, name):
        self.name = name
        print(f"Constructor called. Student {self.name} created.")

    # Destructor
    def __del__(self):
        print(f"Destructor called. Student {self.name} deleted.")


# Creating an object
s1 = Student("Bhavya")

print("Program is running...")

# Deleting the object
del s1