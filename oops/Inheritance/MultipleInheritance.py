class Father:
    def father(self):
        print("Father")


class Mother:
    def mother(self):
        print("Mother")


class Child(Father, Mother):
    def child(self):
        print("Child")


obj = Child()

obj.father()
obj.mother()
obj.child()