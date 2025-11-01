import math

# 1. Check if a year is a leap year
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# 2. Conditional statements exercise
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


# 3. Even numbers between a and b (inclusive)

# Solution 1: with if-else
def even_numbers_with_if(a, b):
    start = a if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1
    if start > end:
        return []
    return list(range(start, end + 1, 2))


# Solution 2: without if-else
def even_numbers_no_if(a, b):
    return list(range(a + a % 2, b + 1, 2))


# Example calls
if __name__ == "__main__":
    print(is_leap(2024))          # True
    check_weird(3)                # Weird
    print(even_numbers_with_if(3, 10))   # [4, 6, 8, 10]
    print(even_numbers_no_if(3, 10))     # [4, 6, 8, 10]
