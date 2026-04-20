#11.Use lambda with reduce() to concatenate a list of strings.
from functools import reduce
words = ["Hello", " ", "World", "!"]
result = reduce(lambda a, b: a + b, words)
print(result)
