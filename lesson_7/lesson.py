# c = 0
# while c <= 10:
#     print(c)
#     c += 1
    
# list_of_tuples = [(1, "Banana"), (2, "Apple"), (3, "Pear")]

# for i, j in list_of_tuples:
#     if (j == "Apple"):
#         print(f"{i} - {j}")
#         break

#     print(f"{i} - {j}")

# ls = [1,2,3,4,5]

# new_ls = [x for x in ls]

# print(new_ls)

# celcius = [12, 8, 19, 22, 34]

# result = [(c * 9/5) + 32 for c in celcius]

# print(result)

password = "12345"

input_password = input("Enter the password: ")

while True:
    if input_password == password:
        break
    input_password = input("Enter the password: ")
