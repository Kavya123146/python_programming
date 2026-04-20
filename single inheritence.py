#single inheritence
class A:
    def one(self):
        print("This is base class")
class B(A):
    def Two(self):
        print("This is derived class")
obj=B()
obj.one()
obj.Two()
