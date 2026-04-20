Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("welcome to python world")
welcome to python world
a=0
print(a)
0
CSE=input("we are CSE-13")
we are CSE-13
CSE=input("enter class strength")
enter class strength58
print(1+2)
3
print(8-4)
4
a=10
print(a)
10
>>> b=20
>>> print(b)
20
>>> sum=a+b
>>> print(sum)
30
>>> print("enter a,b values")
enter a,b values
>>> 2 4
SyntaxError: invalid syntax
>>> a=int(input("enter a value"))
enter a value10
>>> b=int(input("enter b value"))
enter b value4
>>> sum=a+b
>>> print(sum)
14
>>> x,y,z=10,4.2,"hello"
>>> print(x,y,z)
10 4.2 hello
>>> a=2
>>> b=4
>>> c=a+b
>>> print(a and b sum is)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("a and b sum is")
a and b sum is
>>> a and b sum is
SyntaxError: invalid syntax
>>> print("a and b sum is c")
a and b sum is c
>>> print(f"{a} and {b} sum is {c}")
2 and 4 sum is 6
>>> print(f"{a} and {b} sum is"{c})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("{} and{} sum is{}".format(a,b,c))
2 and4 sum is6
>>> a,b=map(int,input("enter a,b values").split)
enter a,b values1 2
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a,b=map(int,input("enter a,b values").split)
TypeError: 'builtin_function_or_method' object is not iterable
>>> a,b=map(int,input("enter a,b values").split())
enter a,b values1 2
