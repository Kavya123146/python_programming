#function arguments
#1.required arguments
def sum(a,b):
    c=a+b
    print(c)
sum(10,20)
#2.default
def sum(x=10,y=30,z=20):
    add=x+y+z
    print(add)
sum(x=10,y=90,z=20)
sum(x=10)
#3.keyword
def sum(x,y=30,z=40):
    addition=x+y+z
    print(addition)
sum(10,50,100)
sum(190)
#4.variable-length
def display(*no):
    print(no)
display(10,20,40)
#5.positional arguments
def greet(name="Hello",age=24):
    print(f'my name is {name} and I am {age} year old')
greet("Hello",24)
greet(24,"Hello")
