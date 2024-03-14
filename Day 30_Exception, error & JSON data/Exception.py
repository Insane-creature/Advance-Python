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
    raise TypeError("I created this error, yes!")
    
# height = float(input("Enter height: "))
# weight = int(input("Enter weight: "))

# if height < 3: 
#     raise ValueError("Humans can't be this big")


# bmi = weight / height ** 2


