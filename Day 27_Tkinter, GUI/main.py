import tkinter

window = tkinter.Tk()
window.title("Home")

window.minsize(width=500, height=300)
my_label = tkinter.Label(text="I'm a Label")
my_label.pack(expand=1)





window.mainloop()