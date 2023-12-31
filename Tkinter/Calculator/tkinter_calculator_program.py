from tkinter import *
from tkinter import messagebox
import tkinter as tk

master = Tk()

# root window title and dimension
master.title("Calculator")

# Start code to center the window

width = 300  # Width
height = 150  # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))

# End code to center the window


# adding a label to the root window
lbl1 = Label(master, text="First Number: ")
lbl2 = Label(master, text="Second Number: ")
lbl3 = Label(master)

lbl1.grid()
lbl2.grid()
lbl3.grid()

# adding Entry Field
txt1 = Entry(master, width=10)
txt1.grid(column=1, row=0)
txt2 = Entry(master, width=10)
txt2.grid(column=1, row=1)
lbl3.grid(column=1, row=2)


# function to display total when
# button is clicked

def show_alert(x):
    messagebox.showinfo(f"Total:", x)

def sum():
    total = float(txt1.get()) + float(txt2.get())
    if total.is_integer():
        res = f"Total: {int(total)}"
        lbl3.configure(text=res)
        show_alert(int(total))
    else:
        res = f"Total: {total}"
        lbl3.configure(text=res)
        show_alert(total)


def divide():
    quotient = float(txt1.get()) / float(txt2.get())
    if quotient.is_integer():
        res = f"Total: {int(quotient)}"
        lbl3.configure(text=res)
        show_alert(int(quotient))
    else:
        res = f"Total: {quotient}"
        lbl3.configure(text=res)
        show_alert(quotient)


def multiply():
    product = float(txt1.get()) * float(txt2.get())
    if product.is_integer():
        res = f"Total: {int(product)}"
        lbl3.configure(text=res)
        show_alert(int(product))
    else:
        res = f"Total: {product}"
        lbl3.configure(text=res)
        show_alert(product)



def subtract():
    sub = float(txt1.get()) - float(txt2.get())
    if sub.is_integer():  # check if sub is a whole number
        res = f"Total: {int(sub)}" # convert sub to int and format it
        print(int(sub))
        lbl3.configure(text=res)
        show_alert(int(sub))
    else:
        res = f"Total: {sub}"  # keep sub as float and format it
        lbl3.configure(text=res)
        show_alert(sub)


button = tk.Button(master, command=show_alert)

# button widget with red color text inside
btn1 = Button(master, text="+", fg="blue", command=sum)
btn2 = Button(master, text="/", fg="blue", command=divide)
btn3 = Button(master, text="*", fg="blue", command=multiply)
btn4 = Button(master, text="-", fg="blue", command=subtract)

# Configure column 0 and 1 to expand and fill any extra space
master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)

# Place the buttons in columns 0 and 1
btn1.grid(column=0, row=4, sticky="nsew")
btn2.grid(column=1, row=4, sticky="nsew")
btn3.grid(column=0, row=6, sticky="nsew")
btn4.grid(column=1, row=6, sticky="nsew")

# Execute Tkinter
master.mainloop()
