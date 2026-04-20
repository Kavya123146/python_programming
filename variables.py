#variables
#1.local variables
def display():
    a=10
    print("inside value is :",a)
display()
#global variables
x=10
def display():
    print("inside fun:",x)
display()
print("outside fun:",x)
#local vs global
x=100
def display():
    x=10
    print("The value for inside:",x)
display()
print("The value for outside:",x)
#change global variable value
y=20
def change():
    global y
    y=40
    print(y)
change()
print(y)


    
