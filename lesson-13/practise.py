# Puzzle 1

# Task:
# Write a program that reverses every word in a given sentence without changing their order.

# Example:
# Input: "Python is fun"
# Output: "nohtyP si nuf"


# answer = input("enter the words: ")

# items = answer.split(" ")

# result = ""


# for i in items:
#     result += i[::-1] + " "

# print(result)

# Puzzle 2

# Task:
# Find the sum of all numbers between 1 and 100 that are divisible by 3.

# Expected Output: 1683

# result = 0

# for i in range(1, 100):
#     if i % 3 == 0:
#         result += i
# print(result)



# Puzzle 3

# Task:
# Remove all vowels from a given string.

# Example:
# Input → "beautiful"
# Output → ['b', 't', 'f', 'l']

# word = input("enter the words: ")

# result = []

# for i in word:
#     if i != 'a' and i != 'i' and i != 'e' and i != 'o' and i != 'u':
#         result.append(i)

# print(result)


# Puzzle 4

# Task:
# Make a list of tuples (x, x²) for numbers 1 to 10.

# Output:
# [(1, 1), (2, 4), (3, 9), ..., (10, 100)]


# result = []

# for i in range(1,11):
#     result.append((i, i*i))

# print(result)



# Puzzle 5

# Task:
# Create a function that will return the longest word in a list.

# Example:
# test('Hello', 'World', 'Hello world')
# Output:
# Hello world


# items = ['Hello', 'World', 'Hello world', "Baxshullajonbekxon"]

# max_item = ""

# for i in items:
#     if len(i) > len(max_item):
#         max_item = i

# print(max_item)