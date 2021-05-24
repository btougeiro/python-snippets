import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Courier", 11, "bold")

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
image_icon = tkinter.PhotoImage(file="logo.png")
window.iconphoto(False, image_icon)

## password generator

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters = [ choice(letters) for _ in range(randint(8, 10)) ]
    pwd_symbols = [ choice(symbols) for _ in range(randint(2, 4)) ]
    pwd_numbers = [ choice(numbers) for _ in range(randint(2, 4)) ]

    password_list = pwd_letters + pwd_symbols + pwd_numbers

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)

## save password to a file

def save():

    if entry_website.get() == "" or entry_password.get() == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=entry_website.get(),
            message=f"These are the details entered: \nEmail: {entry_email.get()} \nPassword: {entry_password.get()} \nIs it OK to save?"
        )

        if is_ok:
            with open(file="data.txt", mode="a") as data_file:
                data_file.write(f"{entry_website.get()} | {entry_email.get()} | {entry_password.get()}\n")
                entry_website.delete(0, tkinter.END)
                entry_password.delete(0, tkinter.END)
                entry_website.focus()

## canvas

canvas = tkinter.Canvas(width=200, height=200)
canvas_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(row=0, column=1)

## labels

label_website = tkinter.Label(text="Website:", font=FONT)
label_website.grid(row=1, column=0)

label_email = tkinter.Label(text="Email/Username:", font=FONT)
label_email.grid(row=2, column=0)

label_password = tkinter.Label(text="Password:", font=FONT)
label_password.grid(row=3, column=0)

## entry

entry_website = tkinter.Entry(width=40, font=FONT)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

entry_email = tkinter.Entry(width=40, font=FONT)
entry_email.insert(0, "test@email.com")
entry_email.grid(row=2, column=1, columnspan=2)

entry_password = tkinter.Entry(width=22, font=FONT)
entry_password.grid(row=3, column=1)

## button

button_generate_password = tkinter.Button(text="Generate Password", font=FONT, width=17, command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = tkinter.Button(text="Add", font=FONT, width=40, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
