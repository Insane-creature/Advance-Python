import pandas
stud_dict = {
    "Student": ["Adam", "Angela", "James"],
    "Scores": [72,45,56]
}

# Looping through dictionary
# for (key, value) in stud_dict.items():
#     print(key, value)
# OUTPUT
# Student ['Adam', 'Angela', 'James']
# Scores [72, 45, 56]

print("####################################")

# Printing values
# for (key, value) in stud_dict.items():
#     print(value)
# OUTPUT
# ['Adam', 'Angela', 'James']
# [72, 45, 56]

####################################

student_data_frame = pandas.DataFrame(stud_dict)
# print(student_data_frame)
#   Student  Scores
# 0    Adam      72
# 1  Angela      45

# LOOPing using pandas
# for (key, value) in student_data_frame.items():
    # print(key)        # Items
    # print(value)
    # 0      Adam
    # 1    Angela
    # 2     James
    # Name: Student, dtype: object
    # 0    72
    # 1    45
    # 2    56
    # print(key, value)


# ITERROWS: loops through rows of dataframes
# for (index, row) in student_data_frame.iterrows():
#     print(row.Scores)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data = {row.letter:row.code for (index, row) in data.iterrows()}

# print(nato_data)

input_letter = ("anshika").upper()


# 1 Way: print(list(input_letter))
# 2 Way: print([*input_letter])
# 3 Way: print([x for x in input_letter])

characters = [spell for spell in [*input_letter]]
output = [nato_data[output_char] for output_char in characters]
# print(output)       # ['Alfa', 'November', 'Sierra', 'Hotel', 'India', 'Kilo', 'Alfa']


