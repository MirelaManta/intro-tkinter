from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # this adds like a frame/ space around the program

# tkinter layout managers -> place(), pack() and grid()


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()  # this method will place a label into the screen and will automatically center it on screen
# my_label.place(x=100, y=0)  # this is too precise, doesn't work when you have hundreds of widgets
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# advanced python arguments
# arg with default values
# *args: Many positional arguments (used when a function can accept any number of arguments)

# **kwargs : Many Keyword Arguments

# Buttons

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="Another button")
button_2.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()  # will keep the window on screen

