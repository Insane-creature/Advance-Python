from tkinter import *

window = Tk()
window.title("Home")
window.minsize(width=500, height=300)
window.config(padx=20, pady= 20)

# Label
my_label = Label(text="I'm a Label")
my_label.grid(column=0, row = 0)

# change the label any value there are two ways
# my_label["text"] = "New Text"
# my_label.config(text="New Anshika")

# Button

def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text = new_text)
   

button1 = Button(text = "Click me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="I am button 2")
button2.grid(column=2, row=0)


# Entry component
input = Entry()
input.grid(column=3, row=4)

print(input.get())



window.mainloop()