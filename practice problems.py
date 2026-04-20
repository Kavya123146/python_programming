#Practice problems
#Easy Level
#1.add two numbers and return the result
def add(a,b):
    return a + b
print(add(1,2))
#2.find the square of a number
def square(n):
    return n * n
print(square(4))
#3.check whether a number is even or odd
def check_even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(4))
#4.print "Hello" 5 times
def print_hello():
    for i in range(5):
        print("Hello")
print_hello()
#5.find the maximum of two numbers
def max_two(a,b):
    if a>b:
        return a
    else:
        return b
print(max_two(10,25))
#Medium Level
#6.find factorial of a number
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))
#7.check whether a number is prime or not
def is_prime(n):
    if n<=1:
       return "not prime"
    for i in range(2,int(n**0.5)+1):
      if n % i == 0:
         return "not prime"
    return "prime"
print(is_prime(11))
#8.find sum of n natural numbers
def sum_n(n):
    return n*(n+1)//2
print(sum_n(5))
#9.reverse a given number
def reverse_number(n):
    rev=0
    while n > 0:
      rev=rev*10+n%10
      n//=10
    return rev
print(reverse_number(1234))
#10.count number of digits in a number
def count_digits(n):
  count=0
  while n>0:
    count+=1
    n//=10
  return count
print(count_digits(12345))



        
        
    

        

    

