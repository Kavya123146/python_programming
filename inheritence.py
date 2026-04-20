#multi-level
class A:
    def one(self):
        print("This is base class")
class B(A):
    def Two(self):
        print("This is derived class")
class C(B):
    def Three(self):
        print("This is another class")
obj=C()
obj.Two()
obj.Three()
