from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# french_text = Label(text="")

df= pd.read_csv("data/french_words.csv")
df_dict = df.to_dict(orient="records")
print(df_dict)

def next_card():
    current_card = random.choice(df_dict)
    canvas.itemconfig(card_title, text = "French")
    canvas.itemconfig(card_word, text = current_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness= 0)
card_front = PhotoImage(file= "images/card_front.png")
canvas.create_image(400, 263, image = card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column= 0,row= 0, columnspan=2)

# card_back = PhotoImage(file= "images/card_back.png")
# canvas.create_image(100, 112, image = card_back)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column= 0,row= 1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column= 1,row= 1)

window.mainloop()