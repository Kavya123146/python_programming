#lambda 13 programs
#1.write a lambda function add two numbers
add = lambda a, b: a + b
print(add(3, 5))
#2.lambda function square of a number
square = lambda x: x * x
print(square(6))
#3.lambda function cube of a number
cube=lambda x:x*x*x
print(cube(2))
#4.lambda function to check whether a number is even or odd
even_odd=lambda x:"Even" if x%2==0 else "Odd"
print(even_odd(4))
#5.lambda function to find the maximum of two numbers
maximum=lambda a,b: a if a>b else b
print(maximum(10,20))
#6.Use lambda with map() to add 5 to each element in a list.
nums=[1,2,3,4,5]
print(list(map(lambda x:x+5,nums)))
#7.Use lambda with map() to multiply corresponding elements of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result = list(map(lambda x, y: x * y, list1, list2))
print(result)
#8.Use lambda with filter() to extract even numbers from a list.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
#9.Use lambda with filter() to extract odd numbers from a list.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)
#10.Use lambda with reduce() to find the minimum element in a list.
from functools import reduce
nums = [10, 5, 8, 2, 15]
minimum = reduce(lambda a, b: a if a < b else b, nums)
print(minimum)
#11.Use lambda with reduce() to concatenate a list of strings.
from functools import reduce
words = ["Hello", " ", "World", "!"]
result = reduce(lambda a, b: a + b, words)
print(result)
#12.Sort numbers in descending order using lambda
nums = [5, 2, 9, 1, 7]
sorted_nums = sorted(nums, key=lambda x: x, reverse=True)
print(sorted_nums)
#13.Use lambda to reverse each string in a list.
words = ["apple", "banana", "cherry"]
reversed_words = list(map(lambda x: x[::-1], words))
print(reversed_words)

