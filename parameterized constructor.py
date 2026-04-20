#parameterized constructor
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is:",self.name)
        print("age is:",self.age)
p1=person("madhu",24)
p1.display()
#addition of two numbers
class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("sum is:",self.a+self.b)
add=add(1,2)
add.display()
