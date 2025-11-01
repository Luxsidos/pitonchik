import random
import string
from datetime import date

# 1. Age Calculator
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = date.today().year
age = current_year - birth_year
print(f"Hello {name}, you are {age} years old.\n")

# 2. Extract Car Names
txt = 'LMaasleitbtui'
car_name = txt[::2]
print("Extracted car name:", car_name)

# 3. Extract Car Names
txt = 'MsaatmiazD'
car_name = txt[::2]
print("Extracted car name:", car_name)

# 4. Extract Residence Area
txt = "I'am John. I am from London"
area = txt.split("from")[-1].strip()
print("Residence area:", area)

# 5. Reverse String
user_str = input("\nEnter a string to reverse: ")
reversed_str = user_str[::-1]
print("Reversed string:", reversed_str)

# 6. Count Vowels
text = input("\nEnter text to count vowels: ").lower()
vowels = 'aeiou'
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

# 7. Find Maximum Value
nums = list(map(int, input("\nEnter numbers separated by spaces: ").split()))
max_value = max(nums)
print("Maximum value:", max_value)

# 8. Check Palindrome
word = input("\nEnter a word to check palindrome: ").lower()
if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# 9. Extract Email Domain
email = input("\nEnter your email address: ")
domain = email.split('@')[-1]
print("Email domain:", domain)

# 10. Generate Random Password
length = int(input("\nEnter desired password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print("Generated password:", password)
