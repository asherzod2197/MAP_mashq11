# 1
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# 2
words = ["hello", "world", "python"]
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)

# 3
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# 4
words = ["hello", "world", "python"]
lengths = list(map(lambda w: len(w), words))
print(lengths)

# 5
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)

# 6
numbers = [-3, -1, 0, 2, -5, 4]
absolutes = list(map(lambda x: abs(x), numbers))
print(absolutes)

# 7
words = ["hello", "world", "python"]
reversed_words = list(map(lambda w: w[::-1], words))
print(reversed_words)
