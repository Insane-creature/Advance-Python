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
    file = open("my_file.txt") 
except: 
    print("There was an error")

