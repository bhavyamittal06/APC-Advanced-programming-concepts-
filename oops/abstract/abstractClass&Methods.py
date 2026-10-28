from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        print("Animal eats")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


d = Dog()
d.sound()
d.eat()