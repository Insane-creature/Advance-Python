from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"   
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20, bg=YELLOW)

canvas = Canvas(width=300, height=400, bg=YELLOW )#, highlightthickness= 0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(150, 200, image = tomato_img)
canvas.create_text(150,215,text="00:00", fill= "white" ,font=(FONT_NAME, 30, "bold"))
canvas.
canvas.grid()

timer = Label(text="Timer")
timer.grid()

window.mainloop()