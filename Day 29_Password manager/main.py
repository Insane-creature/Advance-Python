from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Saving the user data
def save():
    name = textbox1.get()
    useremail = textbox2.get()
    passw = textbox3.get()
    
    with open("userdata.txt", "a") as data:
        data.write(f"{name} | {useremail} | {passw}\n")
        textbox1.delete(0, END)
        textbox3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize(width=400, height= 300)
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo_image)
canvas.grid(column= 1,row=0)

website = Label(text="Website")     # 1,0
website.grid(column= 0,row=1)
website.focus()

textbox1 = Entry(width=38)
textbox1.grid(column= 1,row=1,columnspan=2)
textbox1.focus()

emailuser = Label(text="Email/Username")
emailuser.grid(column= 0,row=2)


textbox2 = Entry(width=38)
textbox2.grid(column= 1,row=2,columnspan=2)
textbox2.insert(0, "anshika@gmail.com")

password = Label(text="Password")
password.grid(column= 0,row=3)

textbox3 = Entry(width=24)
textbox3.grid(column=1 ,row=3)

generatepassword = Label(text="Generate Password")
generatepassword.grid(column= 2,row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column= 1, row=4, columnspan=2)

print(save())

window.mainloop()