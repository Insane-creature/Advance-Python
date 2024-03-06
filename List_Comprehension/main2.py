with open("file1.txt") as file:
    contents1 = file.readlines()

with open("file2.txt") as file:
    contents2 = file.readlines()
    
# result = [n for i in [i for j in i if i == j]]
result = [int(n) for n in contents1 if n in contents2 ]
print(result)