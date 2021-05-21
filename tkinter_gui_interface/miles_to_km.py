import tkinter

## window creation

window = tkinter.Tk()
window.config(padx=5, pady=5)
window.title("Mile to KM Converter")
window.minsize(width=300, height=0)

## convert function

def convert_mile_to_km():
    num_of_miles = float(entry_box.get())
    one_mile_in_km = 1.609344
    calculate = num_of_miles * one_mile_in_km
    label_value_in_km.config(text=f"{calculate:.2f}")

## labels

label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_is_equal_to = tkinter.Label(text="is equal to:")
label_is_equal_to.grid(row=1, column=0)

label_value_in_km = tkinter.Label(text="0")
label_value_in_km.grid(row=1, column=1)

label_km = tkinter.Label(text="Kilometers")
label_km.grid(row=1, column=2)

## button

button_calculate = tkinter.Button(text="Calculate", command=convert_mile_to_km)
button_calculate.grid(row=2, column=1)

## entry

entry_box = tkinter.Entry()
entry_box.config(width=10)
entry_box.grid(row=0, column=1)

## window mainloop

window.mainloop()
