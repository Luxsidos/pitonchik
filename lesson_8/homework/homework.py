
# 1. Handle ZeroDivisionError
def handle_zero_division():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# 2. Handle ValueError for invalid integer input
def handle_value_error():
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
    except ValueError:
        print("Error: That is not a valid integer!")

# 3. Handle FileNotFoundError
def handle_file_not_found():
    try:
        file_name = input("Enter filename: ")
        with open(file_name, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found!")

# 4. Handle TypeError for non-numeric input
def handle_type_error():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
            raise TypeError("Inputs must be numeric!")
        print("Sum:", float(a) + float(b))
    except TypeError as e:
        print("Error:", e)

# 5. Handle PermissionError
def handle_permission_error():
    try:
        file_name = input("Enter filename to open: ")
        with open(file_name, 'w') as f:
            f.write("Testing permission")
    except PermissionError:
        print("Error: You don’t have permission to modify this file!")

# 6. Handle IndexError
def handle_index_error():
    try:
        items = [10, 20, 30]
        index = int(input("Enter index: "))
        print("Item:", items[index])
    except IndexError:
        print("Error: Index out of range!")

# 7. Handle KeyboardInterrupt
def handle_keyboard_interrupt():
    try:
        num = input("Enter a number: ")
        print("You entered:", num)
    except KeyboardInterrupt:
        print("\nInput cancelled by user!")

# 8. Handle ArithmeticError
def handle_arithmetic_error():
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        print(x / y)
    except ArithmeticError as e:
        print("Arithmetic error occurred:", e)

# 9. Handle UnicodeDecodeError
def handle_unicode_decode_error():
    try:
        file_name = input("Enter filename to read: ")
        with open(file_name, 'r', encoding='ascii') as f:
            print(f.read())
    except UnicodeDecodeError:
        print("Error: File has non-ASCII characters!")

# 10. Handle AttributeError
def handle_attribute_error():
    try:
        my_list = [1, 2, 3]
        my_list.push(4)  # push() doesn’t exist in list
    except AttributeError as e:
        print("AttributeError handled:", e)


# ==============================================
# File Input/Output Exercises
# ==============================================

# 1. Read entire text file
def read_entire_file(file_name):
    with open(file_name, 'r') as f:
        print(f.read())

# 2. Read first n lines of a file
def read_first_n_lines(file_name, n):
    with open(file_name, 'r') as f:
        for _ in range(n):
            print(f.readline(), end='')

# 3. Append text to file and display
def append_text(file_name, text):
    with open(file_name, 'a') as f:
        f.write(text + '\n')
    with open(file_name, 'r') as f:
        print(f.read())

# 4. Read last n lines
def read_last_n_lines(file_name, n):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        print(''.join(lines[-n:]))

# 5. Read file line by line into list
def file_to_list(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f]

# 6. Read file line by line into variable
def file_to_variable(file_name):
    with open(file_name, 'r') as f:
        return ''.join(f.readlines())

# 7. Read file into array
def file_to_array(file_name):
    return file_to_list(file_name)

# 8. Find longest words
def find_longest_words(file_name):
    with open(file_name, 'r') as f:
        words = f.read().split()
        max_len = len(max(words, key=len))
        return [w for w in words if len(w) == max_len]

# 9. Count lines in text file
def count_lines(file_name):
    with open(file_name, 'r') as f:
        return len(f.readlines())

# 10. Count frequency of words
def word_frequency(file_name):
    from collections import Counter
    with open(file_name, 'r') as f:
        words = f.read().replace(',', ' ').split()
        return Counter(words)

# 11. Get file size
def get_file_size(file_name):
    import os
    return os.path.getsize(file_name)

# 12. Write list to file
def write_list_to_file(file_name, data_list):
    with open(file_name, 'w') as f:
        for item in data_list:
            f.write(str(item) + '\n')

# 13. Copy contents to another file
def copy_file(source, dest):
    with open(source, 'r') as src, open(dest, 'w') as dst:
        dst.write(src.read())

# 14. Combine lines from two files
def combine_files(file1, file2, output):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
        for line1, line2 in zip(f1, f2):
            out.write(line1.strip() + " " + line2)

# 15. Read random line
import random
def random_line(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# 16. Check if file is closed
def is_file_closed(file_name):
    f = open(file_name, 'r')
    print("Closed before:", f.closed)
    f.close()
    print("Closed after:", f.closed)

# 17. Remove newline characters
def remove_newlines(file_name):
    with open(file_name, 'r') as f:
        text = f.read().replace('\n', '')
    return text

# 18. Count number of words
def count_words(file_name):
    with open(file_name, 'r') as f:
        text = f.read().replace(',', ' ')
        return len(text.split())

# 19. Extract characters into list
def extract_characters(file_name):
    with open(file_name, 'r') as f:
        return list(f.read())

# 20. Generate A–Z text files
def generate_alphabet_files():
    import string
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as f:
            f.write(f"This is file {letter}.txt")

# 21. Create alphabet file with N letters per line
def create_alphabet_file(filename, letters_per_line=5):
    import string
    letters = string.ascii_uppercase
    with open(filename, 'w') as f:
        for i in range(0, len(letters), letters_per_line):
            f.write(letters[i:i+letters_per_line] + '\n')


# ==============================================
if __name__ == "__main__":
    print("All Exception and File I/O exercises are ready for testing.")
    # Example quick test:
    # handle_zero_division()
    # read_entire_file("example.txt")
