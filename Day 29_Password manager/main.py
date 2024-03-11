from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize(width=400, height= 300)
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo_image)
canvas.grid(column= 1,row=0)

website = Label(text="Website")     # 1,0
website.grid(column= 0,row=1)

textbox1 = Entry(width=35)
textbox1.grid(column= 1,row=1,columnspan=2)

emailuser = Label(text="Email/Username")
emailuser.grid(column= 0,row=2)

textbox2 = Entry(width=35)
textbox2.grid(column= 1,row=2,columnspan=2)

password = Label(text="Password")
password.grid(column= 0,row=3)

textbox3 = Entry(width=21)
textbox3.grid(column=1 ,row=3)

generatepassword = Label(text="Generate Password")
generatepassword.grid(column= 2,row=3)

add = Button(text="Add", width=36)
add.grid(column= 1, row=4, columnspan=2)



window.mainloop()