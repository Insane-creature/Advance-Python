# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato.txt")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only alphabets")
else:
    print(output_list)

