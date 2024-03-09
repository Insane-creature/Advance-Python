from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady= 20)

def convert_milestokm():
    mile = float(Inputo.get())
    km = mile * 1.61
    km_result_label.config(text=f"{km}")

# def button_clicked():
#     convert_milestokm()

Inputo = Entry(width=7)
Inputo.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Enter: ")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text=0)
km_result_label.grid(column= 1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert_milestokm)
button.grid(column=1, row=2)


window.mainloop()