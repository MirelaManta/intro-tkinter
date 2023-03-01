from tkinter import *


def calculate_button():
    miles = float(miles_input.get())
    km = miles * 1.609344
    result_rounded = round(km, 2)
    result.config(text=f"{result_rounded}")


FONT = ("Times New Roman", 14, "bold")
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=280, height=150)
window.config(padx=20, pady=20)


miles_input = Entry(width=14)
miles_input.grid(column=1, row=0)


label = Label(text="is equal to", font=FONT)
label.grid(column=0, row=1)
label.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

result = Label(text="0", font=FONT)
result.grid(column=1, row=1)
result.config(padx=20, pady=20)

button = Button(text="Calculate", font=FONT, command=calculate_button)
button.grid(column=1, row=2)

window.mainloop()