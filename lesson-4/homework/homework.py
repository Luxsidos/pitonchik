# DICTIONARY EXERCISES


# 1. Sort a Dictionary by Value
d = {'a': 3, 'b': 1, 'c': 2}
asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

# 2. Add a Key to a Dictionary
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("After adding key:", sample_dict)

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:", merged_dict)

# 4. Generate a Dictionary with Squares
n = 5
square_dict = {x: x ** 2 for x in range(1, n + 1)}
print("Dictionary with squares (1 to n):", square_dict)

# 5. Dictionary of Squares (1 to 15)
square_dict_15 = {x: x ** 2 for x in range(1, 16)}
print("Dictionary with squares (1 to 15):", square_dict_15)


# SET EXERCISES

# 1. Create a Set
my_set = {1, 2, 3, 4, 5}
print("\nCreated set:", my_set)

# 2. Iterate Over a Set
print("Iterating over set elements:")
for item in my_set:
    print(item)

# 3. Add Member(s) to a Set
my_set.add(6)
my_set.update([7, 8])
print("After adding members:", my_set)

# 4. Remove Item(s) from a Set
my_set.remove(3)
print("After removing 3:", my_set)

# 5. Remove an Item if Present in the Set
my_set.discard(10) 
print("After safely removing 10 (if exists):", my_set)
