class A:
    def show_a(self):
        print("A")


class B(A):
    def show_b(self):
        print("B")


class C(A):
    def show_c(self):
        print("C")


class D(B, C):
    def show_d(self):
        print("D")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()