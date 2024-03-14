from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(height=400, width=400, padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=400, height=400, bg=BACKGROUND_COLOR, highlightthickness= 0)

# card_back = PhotoImage(file= "card_back.png")
card_front = PhotoImage(file= "card_front.png")

canvas.create_image(100, 112, image = card_front)
# canvas.create_image(100, 112, image = tomato_img)


window.mainloop()