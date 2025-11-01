# math_operations.py 
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


# string_utils.py 
class StringUtils:
    @staticmethod
    def reverse_string(s):
        return s[::-1]

    @staticmethod
    def count_vowels(s):
        vowels = "aeiouAEIOU"
        return sum(1 for ch in s if ch in vowels)


# ===== geometry/circle.py =====
class Geometry:
    class Circle:
        @staticmethod
        def calculate_area(radius):
            return 3.14159 * radius ** 2

        @staticmethod
        def calculate_circumference(radius):
            return 2 * 3.14159 * radius


# ===== file_operations/file_reader.py
class FileOperations:
    class FileReader:
        @staticmethod
        def read_file(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    return file.read()
            except FileNotFoundError:
                return "File not found."

    # file_operations/file_writer.py 
    class FileWriter:
        @staticmethod
        def write_file(file_path, content):
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            return "File written successfully."


# main.py
if __name__ == "__main__":
    print("=== Custom Modules & Packages Demo ===\n")

    # Math Operations
    print("Math Operations:")
    print("Add:", MathOperations.add(10, 5))
    print("Subtract:", MathOperations.subtract(10, 5))
    print("Multiply:", MathOperations.multiply(10, 5))
    print("Divide:", MathOperations.divide(10, 5))

    print("\nString Utilities:")
    text = "Hello World"
    print("Reverse:", StringUtils.reverse_string(text))
    print("Vowel Count:", StringUtils.count_vowels(text))

    print("\nGeometry - Circle:")
    radius = 5
    print("Area:", Geometry.Circle.calculate_area(radius))
    print("Circumference:", Geometry.Circle.calculate_circumference(radius))

    print("\nFile Operations:")
    path = "sample.txt"
    content = "This is a test file."
    print(FileOperations.FileWriter.write_file(path, content))
    print("File content:", FileOperations.FileReader.read_file(path))
