from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=400, height=425, bg=BACKGROUND_COLOR, highlightthickness= 0)

card_back = PhotoImage(file= "images/card_back.png")
card_front = PhotoImage(file= "images/card_front.png")

canvas.create_image(100, 112, image = card_front)
canvas.create_image(100, 112, image = card_back)
canvas.grid(column= 0,row= 0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column= 0,row= 1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column= 1,row= 1)

window.mainloop()