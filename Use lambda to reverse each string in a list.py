#13.Use lambda to reverse each string in a list.
words = ["apple", "banana", "cherry"]
reversed_words = list(map(lambda x: x[::-1], words))
print(reversed_words)

