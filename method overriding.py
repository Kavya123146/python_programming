#method overriding
class mother:
    def parent(self):
        print("This is base class")
class child(mother):
    def parent(self):
        super().parent()
        print("This is child class")
ch=child()
ch.parent()
