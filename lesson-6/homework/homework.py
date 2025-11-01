# 1. Modify String with Underscores
def modify_with_underscores(txt):
    vowels = "aeiouAEIOU"
    result = ""
    i = 0
    count = 0

    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3 and i != len(txt) - 1:
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == "_"):
                result += txt[i + 1] if i + 1 < len(txt) else ""
                i += 1
            else:
                result += "_"
            count = 0
        i += 1
    return result


# 2. Integer Squares Exercise

def print_squares(n):
    for i in range(n):
        print(i ** 2)


# 3. Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers using a while loop
def print_natural_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1


# Exercise 2: Print the following pattern
def print_pattern():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# Exercise 3: Calculate sum of all numbers from 1 to a given number
def sum_numbers(n):
    total = sum(range(1, n + 1))
    print("Sum is:", total)


# Exercise 4: Print multiplication table of a given number
def multiplication_table(num):
    for i in range(1, 11):
        print(num * i)


# Exercise 5: Display numbers from a list using a loop
def filter_numbers(numbers):
    for num in numbers:
        if num > 500:
            break
        if num % 5 == 0 and num <= 150:
            print(num)


# Exercise 6: Count the total number of digits in a number
def count_digits(num):
    print(len(str(num)))


# Exercise 7: Print reverse number pattern
def reverse_number_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


# Exercise 8: Print list in reverse order using a loop
def print_list_reverse(lst):
    for i in reversed(lst):
        print(i)


# Exercise 9: Display numbers from -10 to -1 using a for loop
def print_negative_range():
    for i in range(-10, 0):
        print(i)


# Exercise 10: Display message “Done” after successful loop execution
def print_done():
    for i in range(5):
        print(i)
    print("Done!")


# Exercise 11: Print all prime numbers within a range
def print_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)


# Exercise 12: Display Fibonacci series up to 10 terms
def fibonacci_series(n=10):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end="  ")
        a, b = b, a + b
    print()


# Exercise 13: Find the factorial of a given number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{n}! =", result)


# 4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    result = [x for x in list1 if x not in list2] + [y for y in list2 if y not in list1]
    return result


# Example test calls
if __name__ == "__main__":
    print("1.", modify_with_underscores("abcabcabcdeabcdefabcdefg"))
    print("\n2.")
    print_squares(5)
    print("\n3.1")
    print_natural_numbers()
    print("\n3.2")
    print_pattern()
    print("\n3.3")
    sum_numbers(10)
    print("\n3.4")
    multiplication_table(2)
    print("\n3.5")
    filter_numbers([12, 75, 150, 180, 145, 525, 50])
    print("\n3.6")
    count_digits(75869)
    print("\n3.7")
    reverse_number_pattern(5)
    print("\n3.8")
    print_list_reverse([10, 20, 30, 40, 50])
    print("\n3.9")
    print_negative_range()
    print("\n3.10")
    print_done()
    print("\n3.11")
    print_primes(25, 50)
    print("\n3.12")
    fibonacci_series()
    print("\n3.13")
    factorial(5)
    print("\n4.")
    print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))
