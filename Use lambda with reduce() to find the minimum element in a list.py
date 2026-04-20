#10.Use lambda with reduce() to find the minimum element in a list.
from functools import reduce
nums = [10, 5, 8, 2, 15]
minimum = reduce(lambda a, b: a if a < b else b, nums)
print(minimum)
