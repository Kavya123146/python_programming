#9.Use lambda with filter() to extract odd numbers from a list.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)
