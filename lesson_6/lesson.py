# number = int(input("enter number: "))

# if number % 2 == 0:
#     print("your number is even")
# else:
#     print("your number is odd")


# a = int(input("enter number: "))
# b = int(input("enter number: "))
# c = int(input("enter number: "))


# if a > b and a > c:
#     print("A maximum")
# elif b > c and b > a:
#     print("B maximum")
# elif c > b and c > a:
#     print("C maximum")
# elif a == b and b > c:
#     print("A and B maximum")
# elif a == c and c > b:
#     print("A and C maximum")
# else:
#     print("THEY EQUAL")

# price = int(input("Enter the price: "))

# if price >= 1000:
#     print(f"you must pay: {price * .8}")
# elif price >= 500:
#     print(f"you must pay: {price * .9}")
# else:
#     print(f"you must pay: {price}")


password = input("Enter the password: ")

if len(password) > 5 and password.find(" ") == -1:
    print("You entered valid password!")
else:
    print("Incorrect!")

# ALTERNATIVE
if len(password) > 5 and password not in " ":
    print("You entered valid password!")
else:
    print("Incorrect!")


    