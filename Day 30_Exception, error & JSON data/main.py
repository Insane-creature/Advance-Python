# FileNotFoundError
# with open("my_file.txt") as file:
#     file.read()

# Key Error
a_dict = {"key":"value"}
# value = a_dict["non_existential_key"]

# IndexError
fruits = ["Apple", "Banana","Orange"]
# fruit = fruits[3]

# Type Error
text = "abc"
# print(text)

try:
    file = open("create_file.txt") 
    a_dict = {"key":"value"}
    print(a_dict["ksfksjf"])
except FileNotFoundError: 
    file = open("create_file.txt","w")
    print("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file is closed.")
