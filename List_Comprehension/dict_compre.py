import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(50,100) for student in names}

# print(type(names))
# print(type(student_scores))
# print(student_scores)

passed_students = { name:score for (name,score) in student_scores.items() if score >=60 }
# print(passed_students)

sentence = "What is he studying lately?"

# word = {word for word in sentence.split()}      # {'he', 'studying', 'lately?', 'is', 'What'}
# word = {print(word) for word in sentence.split()}   # What is he studying lately?  --> all words in newline


word_letter_counter = {word:len(word) for word in sentence.split() }
print(word_letter_counter)


