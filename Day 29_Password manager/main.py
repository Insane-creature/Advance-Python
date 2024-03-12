from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password5 = "".join(password_list)
    textbox3.insert(0, password5)
    pyperclip.copy(password5)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Saving the user data
def save():
    website_name = textbox1.get()
    useremail = textbox2.get()
    passw = textbox3.get()
    
    if len(website_name) != 0 and len(useremail) != 0 or len(passw) != 0: 
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {useremail} "
                                    f"\nPassword: {passw} \nIs it okay to save?")
        if is_ok:
            with open("userdata.txt", "a") as data:
                data.write(f"{website_name} | {useremail} | {passw}\n")
                textbox1.delete(0, END)
                textbox3.delete(0, END)
    else:
        messagebox.showerror(title="Error found", message= "You left some of the fields emplty, please check.")
        
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

generatepassword = Button(text="Generate Password", command=generate_password)
generatepassword.grid(column= 2,row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column= 1, row=4, columnspan=2)

print(save())

window.mainloop()