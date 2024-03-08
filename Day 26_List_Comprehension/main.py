numbers = [1,2,3]
# print(numbers)
new_list = [n+2 for n in numbers]
# print(new_list)

name = "Anshika"
new_name = [letters for letters in name]
# print(new_name)

range_list = [n*2 for n in range(1,5)]
# print(range_list)

short_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
cap_names = [name.upper() for name in short_names if len(name) > 5]
print(cap_names)

numbers1 = [1,1,2,3,5,8,13,21]
squarred_numbers = [sn * sn for sn in numbers]
# print(squarred_numbers)

numbers = input().split(',')
# even_num = [num for num in numbers if num % 2 == 0]
even_num = [int(x) for x in numbers]
# print(numbers)


