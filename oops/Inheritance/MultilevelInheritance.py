class Grandfather:
    def grandfather(self):
        print("Grandfather")


class Father(Grandfather):
    def father(self):
        print("Father")


class Child(Father):
    def child(self):
        print("Child")


obj = Child()

obj.grandfather()
obj.father()
obj.child()