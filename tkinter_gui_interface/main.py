import tkinter

def button_clicked():
    label_1.config(text=entry_1.get())

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=640, height=480)
window.config(padx=5, pady=5)

## Label
label_1 = tkinter.Label(text="Initial Label Text")
label_1.grid(row=0, column=0)

## Buttons
button_1 = tkinter.Button(text="button_1", command=button_clicked)
button_1.grid(row=1, column=1)

button_2 = tkinter.Button(text="button_2")
button_2.grid(row=0, column=2)

## Entry
entry_1 = tkinter.Entry(width=10)
entry_1.grid(row=2, column=3)

# we have three kinds of placement... you can only use one of them in your program
# grid
# place
# pack

window.mainloop()
