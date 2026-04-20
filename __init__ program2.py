#example 1:
class display:
    def __init__(self,name):
        self.name=name
d1=display("Hi")
print(d1)
#example 2:
class display:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "student name is:" + self.name
d1=display("silence")
print(d1)

