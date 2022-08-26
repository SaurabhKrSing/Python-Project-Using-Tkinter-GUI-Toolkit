# importing Libraries
from tkinter import *
import random
import string
import pyperclip
from PIL import ImageTk, Image

# initialize window
root = Tk()

# Background
root.configure(bg='black')

# Title bar Icon
root.iconbitmap('icon.ico')

# Title bar Name
root.title("Password Generator Application")

# Heading
heading = Label(root, text='PASSWORD GENERATOR TOOL',
                font='arial 28 bold', foreground='red', bg="black").pack(pady=15)

# Paragraph
leftside = Label(text='''Need a Unique,\nSecure Password?''',
                 font='arial 30 bold', bg='black', fg='yellow', padx=5, pady=5).pack()

Bootom = Label(root, text='Saurabh Kumar Singh',
               font='arial 10 bold', foreground='white', bg='black').pack(side=BOTTOM, pady=10, fill=X)

# select password length
pass_label = Label(root, text='Please Select Password Length',
                   font='arial 20 bold', foreground='white', bg='black').pack(padx=10, pady=10, side=TOP)
pass_len = IntVar()
length = Spinbox(root, from_=5, to_=40, font='arial 20 bold', textvariable=pass_len,
                 width=3).pack(ipadx=3, ipady=3)


# define function
pass_str = StringVar()


# Generate Function
def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase)+random.choice(
            string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password+random.choice(string.ascii_uppercase +
                                          string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


# Generate Button
Button(root, text="GENERATE", font='arial 10 bold',
       command=Generator).pack(pady=20)

Entry(root, textvariable=pass_str, font='arial 10 bold',
      width=42).pack(ipadx=5, ipady=5)


# function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())


# Copy Button
Button(root, text='COPY TO CLIPBOARD', font='arial 10 bold',
       command=Copy_password).pack(pady=20, padx=30)


# loop to run program
root.mainloop()
