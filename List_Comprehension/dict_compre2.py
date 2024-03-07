whether_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 13,
    "Friday": 18,
    "Saturday": 12
}

whether_f = { day:temp*1.8+32 for (day,temp) in whether_c.items()}
print(whether_f)

# f = (c*1.8) + 32