class Student:
    def __init__(self):
        self.name = "Tejas"
        self._age = 20
        self.__marks = 100
        
    def display(self):
        print("Name : ", self.name)
        print("Age : ", self._age)
        print("Marks : ", self.__marks)
            
s = Student()

print(s.name)
print(s._age)
s.display()