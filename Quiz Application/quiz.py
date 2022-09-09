import time
import random
import sqlite3
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.iconbitmap('quiz.ico')
    login.title('Quiz Application Login Page')

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login, width=1570, height=900, bg="black")
    login_canvas.pack()
    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="🎓 Login your account for Quiz 🎓",
                    fg="blue", bg="white")
    heading.config(font=('Arial 40 bold'))
    heading.place(relx=0.1, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Username",
                   font='Arial 25 bold', fg='black', bg='white')
    ulabel.place(relx=0.15, rely=0.4)
    uname = Entry(login_frame, font='Arial 25 bold', bg='white',
                  fg='black', textvariable=user_name)
    uname.config(width=30)
    uname.place(relx=0.31, rely=0.4)

    # PASSWORD
    plabel = Label(login_frame, text="Password",
                   font='Arial 25 bold', fg='black', bg='white')
    plabel.place(relx=0.150, rely=0.5)
    pas = Entry(login_frame, font='Arial 25 bold', bg='white', fg='black',
                textvariable=password, show="*")
    pas.config(width=30)
    pas.place(relx=0.31, rely=0.5)

    def check():
        for a, b, c, d in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)

                menu(a)
                break
        else:
            error = Label(
                login_frame, text="Wrong Username or Password!", font='Arial 15 bold', fg='red', bg='white')
            error.place(relx=0.39, rely=0.9)

    # LOGIN BUTTON
    log = Button(login_frame, text='Login', font='Arial 20 bold',
                 padx=5, pady=5, width=5, command=check, fg="white", bg="red")
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.4, rely=0.7)

    login.mainloop()


def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.iconbitmap('quiz.ico')
    sup.title('Quiz Application Login & Sign Up')

    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()

    sup_canvas = Canvas(sup, width=1570, height=900, bg="black")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="White")
    sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(
        sup_frame, text="🎓 Register your account for Quiz 🎓", fg="#0000cc", bg="White")
    heading.config(font=('Arial 50 bold'))
    heading.place(relx=0, rely=0.1)

    # full name
    flabel = Label(sup_frame, text="Full Name",
                   font='Arial 25 bold', fg='black', bg='white')
    flabel.place(relx=0.15, rely=0.4)
    fname = Entry(sup_frame, font='Arial 25 bold',
                  bg='white', fg='black', textvariable=fname)
    fname.config(width=30)
    fname.place(relx=0.31, rely=0.4)

    # username
    ulabel = Label(sup_frame, text="Username",
                   font='Arial 25 bold', fg='black', bg='white')
    ulabel.place(relx=0.15, rely=0.5)
    user = Entry(sup_frame, font='Arial 25 bold',
                 bg='white', fg='black', textvariable=uname)
    user.config(width=30)
    user.place(relx=0.31, rely=0.5)

    # password
    plabel = Label(sup_frame, font='Arial 25 bold',
                   text="Password", fg='black', bg='white')
    plabel.place(relx=0.150, rely=0.6)
    pas = Entry(sup_frame, font='Arial 25 bold', bg='white', fg='black',
                textvariable=passW, show="*")
    pas.config(width=30)
    pas.place(relx=0.31, rely=0.6)

    # country
    clabel = Label(sup_frame, font='Arial 25 bold',
                   text="Country", fg='black', bg='white')
    clabel.place(relx=0.150, rely=0.7)
    c = Entry(sup_frame, font='Arial 25 bold', bg='white',
              fg='black', textvariable=country)
    c.config(width=30)
    c.place(relx=0.31, rely=0.7)

    def addUserToDataBase():

        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()

        if len(fname.get()) == 0 and len(user.get()) == 0 and len(pas.get()) == 0 and len(c.get()) == 0:
            error = Label(
                text="You haven't enter any field...Please Enter all the fields", font='Arial 15 bold', fg='red', bg='white')
            error.place(relx=0.4, rely=0.7)

        elif len(fname.get()) == 0 or len(user.get()) == 0 or len(pas.get()) == 0 or len(c.get()) == 0:
            error = Label(text="Please Enter all the fields",
                          font='Arial 15 bold', fg='red', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(
                text="Username and password can't be empty", font='Arial 15 bold', fg='red', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0:
            error = Label(text="Username can't be empty", font='Arial 15 bold',
                          fg='red', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",
                          fg='red', bg='white')
            error.place(relx=0.37, rely=0.7)

        else:

            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute(
                'CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",
                           (fullname, username, password, country))
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z = create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)

    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        loginPage(z)

    # signup BUTTON
    sp = Button(sup_frame, text='Sign Up', font='Arial 20 bold', padx=5, pady=5, width=5,
                command=addUserToDataBase, bg="red", fg="white")
    sp.configure(width=15, height=1, activebackground="black", relief=SUNKEN)
    sp.place(relx=0.4, rely=0.8)

    log = Button(sup_frame, text='Already have a Account?', font='Arial 20 bold',
                 padx=5, pady=5, width=5, command=gotoLogin, bg='white', fg="blue")
    log.configure(width=20, height=1, activebackground='white', relief=FLAT)
    log.place(relx=0.370, rely=0.9)

    sup.mainloop()


def menu(abcdefgh):
    login.destroy()
    global menu
    menu = Tk()
    menu.iconbitmap('quiz.ico')
    menu.title('Quiz Application Menu')

    menu_canvas = Canvas(menu, width=1570, height=900, bg="black")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas, bg="white")
    menu_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(menu_canvas, text=' W E L C O M E    T O    Q U I Z    A P P L I C A T I O N ',
                fg="yellow", bg="black")
    wel.config(font=('Arial 30 bold'))
    wel.place(relx=0.18, rely=0.02)

    abcdefgh = 'Welcome ' + abcdefgh
    level34 = Label(menu_frame, text=abcdefgh, font='Arial 40 bold', bg="white",
                    fg="#0000ff")
    level34.place(relx=0.15, rely=0.1)

    level = Label(menu_frame, text='Select your Difficulty Level !!', font="Arial 30 bold", fg='#8800cc',
                  bg="white")
    level.place(relx=0.25, rely=0.3)

    var = IntVar()
    easyR = Radiobutton(menu_frame, text='Easy', bg="white", fg='green',
                        font="Arial 20 bold", value=1, variable=var)
    easyR.place(relx=0.25, rely=0.4)

    mediumR = Radiobutton(menu_frame, text='Medium',
                          bg="white", fg='orange', font="Arial 20 bold", value=2, variable=var)
    mediumR.place(relx=0.25, rely=0.5)

    hardR = Radiobutton(menu_frame, text='Hard', bg="white", fg='red',
                        font="Arial 20 bold", value=3, variable=var)
    hardR.place(relx=0.25, rely=0.6)

    def navigate():

        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()

        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame, text="Let's Go", bg="black",
                    fg="white", font="Arial 20 bold", command=navigate)
    letsgo.place(relx=0.25, rely=0.8)
    menu.mainloop()


def easy():

    global e
    e = Tk()
    e.iconbitmap('quiz.ico')
    e.title('Quiz App - Easy Level')

    easy_canvas = Canvas(e, width=1570, height=900, bg="green")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas, bg="white")
    easy_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(10, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return (-1)
        else:
            return 0
    global score
    score = 0

    easyQ = [
        [
            "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
            "[1, 0, 2, ‘hello’, '', []]",
            "Error",
            "[1, 2, ‘hello’]",
            "[1, 0, 2, 0, ‘hello’, '', []]"
        ],
        [
            "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)",
            "34.00",
            "34.000000",
            "34.0000",
            "34.00000000"

        ],
        [
            "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10",
            "30.8",
            "27.2",
            "28.4",
            "30.0"
        ],
        [
            "Which of these in not a core data type?",
            "Tuples",
            "Dictionary",
            "Lists",
            "Class"
        ],
        [
            "Which of the following represents the bitwise XOR operator?",
            "&",
            "!",
            "^",
            "|"
        ]
    ]
    answer = [
        "[1, 2, ‘hello’]",
        "34.000000",
        "27.2",
        "Class",
        "^"
    ]
    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(easy_frame, text=easyQ[x]
                 [0], font="Arial 20 bold", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(easy_frame, text=easyQ[x][1], font="Arial 20 bold",
                    value=easyQ[x][1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(easy_frame, text=easyQ[x][2], font="Arial 20 bold",
                    value=easyQ[x][2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(easy_frame, text=easyQ[x][3], font="Arial 20 bold",
                    value=easyQ[x][3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(easy_frame, text=easyQ[x][4], font="Arial 20 bold",
                    value=easyQ[x][4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    li.remove(x)

    timer = Label(e)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():

        if len(li) == 1:
            e.destroy()
            showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=easyQ[x][0])

            a.configure(text=easyQ[x][1], value=easyQ[x][1])

            b.configure(text=easyQ[x][2], value=easyQ[x][2])

            c.configure(text=easyQ[x][3], value=easyQ[x][3])

            d.configure(text=easyQ[x][4], value=easyQ[x][4])

            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        if (var.get() in answer):
            score += 1
        display()

    submit = Button(easy_frame, command=calc,
                    text="Submit", font='Arial 20 bold', fg="black", bg="red")
    submit.place(relx=0.5, rely=0.94, anchor=CENTER)

    next_img = Image.open('next.jpg')
    next_btn = ImageTk.PhotoImage(next_img)
    nextQuestion = Button(easy_frame, command=display,
                          image=next_btn, highlightthickness=0, font='Arial 20 bold', fg="white", bg="black")
    nextQuestion.place(relx=0.95, rely=0.91, anchor=CENTER)

#    pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
#    pre.place(relx=0.75, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    e.mainloop()


def medium():

    global m
    m = Tk()
    m.iconbitmap('quiz.ico')
    m.title('Quiz Application - Medium Level')

    med_canvas = Canvas(m, width=1570, height=900, bg="orange")
    med_canvas.pack()

    med_frame = Frame(med_canvas, bg="white")
    med_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(10, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    score = 0

    mediumQ = [
        [
            "Which of the following is not an exception handling keyword in Python?",
            "accept",
            "finally",
            "except",
            "try"
        ],
        [
            "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
            "3",
            "5",
            "25",
            "1"
        ],
        [
            "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
            "Error",
            "None",
            "25",
            "2"
        ],
        [
            "print(0xA + 0xB + 0xC):",
            "0xA0xB0xC",
            "Error",
            "0x22",
            "33"
        ],
        [
            "Which of the following is invalid?",
            "_a = 1",
            "__a = 1",
            "__str__ = 1",
            "none of the mentioned"
        ],
    ]
    answer = [
        "accept",
        "1",
        "25",
        "33",
        "none of the mentioned"
    ]

    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(med_frame, text=mediumQ[x]
                 [0], font="Arial 20 bold", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(med_frame, text=mediumQ[x][1], font="Arial 20 bold",
                    value=mediumQ[x][1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med_frame, text=mediumQ[x][2], font="Arial 20 bold",
                    value=mediumQ[x][2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med_frame, text=mediumQ[x][3], font="Arial 20 bold",
                    value=mediumQ[x][3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med_frame, text=mediumQ[x][4], font="Arial 20 bold",
                    value=mediumQ[x][4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    li.remove(x)

    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():

        if len(li) == 1:
            m.destroy()
            showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=mediumQ[x][0])

            a.configure(text=mediumQ[x][1], value=mediumQ[x][1])

            b.configure(text=mediumQ[x][2], value=mediumQ[x][2])

            c.configure(text=mediumQ[x][3], value=mediumQ[x][3])

            d.configure(text=mediumQ[x][4], value=mediumQ[x][4])

            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        if (var.get() in answer):
            score += 1
        display()

    submit = Button(med_frame, command=calc,
                    text="Submit", font='Arial 20 bold', fg="black", bg="red")
    submit.place(relx=0.5, rely=0.94, anchor=CENTER)

    next_img = Image.open('next.jpg')
    next_btn = ImageTk.PhotoImage(next_img)
    nextQuestion = Button(med_frame, command=display,
                          image=next_btn, highlightthickness=0, font='Arial 20 bold',  fg="white", bg="black")
    nextQuestion.place(relx=0.95, rely=0.91, anchor=CENTER)

   # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    m.mainloop()


def difficult():

    global h
    # count=0
    h = Tk()
    h.iconbitmap('quiz.ico')
    h.title('Quiz Application - Hard Level')

    hard_canvas = Canvas(h, width=1570, height=900, bg="red")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas, bg="white")
    hard_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(10, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    score = 0

    hardQ = [
        [
            "All keywords in Python are in _________",
            "lower case",
            "UPPER CASE",
            "Capitalized",
            "None of the mentioned"
        ],
        [
            "Which of the following cannot be a variable?",
            "__init__",
            "in",
            "it",
            "on"
        ],
        [
            "Which of the following is a Python tuple?",
            "[1, 2, 3]",
            "(1, 2, 3)",
            "{1, 2, 3}",
            "{}"
        ],
        [
            "What is returned by math.ceil(3.4)?",
            "3",
            "4",
            "4.0",
            "3.0"
        ],
        [
            "What will be the output of print(math.factorial(4.5))?",
            "24",
            "120",
            "error",
            "24.0"
        ]

    ]
    answer = [
        "None of the mentioned",
        "in",
        "(1,2,3)",
        "4",
        "error"
    ]

    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(hard_frame, text=hardQ[x]
                 [0], font="Arial 20 bold", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(hard_frame, text=hardQ[x][1], font="Arial 20 bold",
                    value=hardQ[x][1], variable=var, bg="white", fg="black")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(hard_frame, text=hardQ[x][2], font="Arial 20 bold",
                    value=hardQ[x][2], variable=var, bg="white", fg="black")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(hard_frame, text=hardQ[x][3], font="Arial 20 bold",
                    value=hardQ[x][3], variable=var, bg="white", fg="black")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(hard_frame, text=hardQ[x][4], font="Arial 20 bold",
                    value=hardQ[x][4], variable=var, bg="white", fg="black")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    li.remove(x)

    timer = Label(h)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():

        if len(li) == 1:
            h.destroy()
            showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=hardQ[x][0])

            a.configure(text=hardQ[x][1], value=hardQ[x][1])

            b.configure(text=hardQ[x][2], value=hardQ[x][2])

            c.configure(text=hardQ[x][3], value=hardQ[x][3])

            d.configure(text=hardQ[x][4], value=hardQ[x][4])

            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        # count=count+1
        if (var.get() in answer):
            score += 1
        display()

   # def lastPage():
    #    h.destroy()
     #   showMark()

    submit = Button(hard_frame, command=calc,
                    text="Submit", font='Arial 20 bold', fg="black", bg="red")
    submit.place(relx=0.5, rely=0.94, anchor=CENTER)

    next_img = Image.open('next.jpg')
    next_btn = ImageTk.PhotoImage(next_img)

    nextQuestion = Button(hard_frame, command=display,
                          image=next_btn, highlightthickness=0, font='Arial 20 bold', fg="white", bg="black")
    nextQuestion.place(relx=0.94, rely=0.91, anchor=CENTER)

    #pre=Button(hard_frame,command=display, text="Previous", fg="white", bg="black")
    #pre.place(relx=0.75, rely=0.82, anchor=CENTER)

   # end=Button(hard_frame,command=showMark(m), text="End", fg="white", bg="black")
    # end.place(relx=0.8, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    h.mainloop()


def showMark(mark):
    sh = Tk()
    sh.iconbitmap('quiz.ico')
    sh.title('Your Marks')

    st = "Your score is "+str(mark)+"/5"
    mlabel = Label(sh, text=st)
    mlabel.pack()

    def callsignUpPage():
        sh.destroy()
        start()

    def myeasy():
        sh.destroy()
        easy()

    b24 = Button(text="Re-attempt", font='Arial 20 bold',
                 command=myeasy, bg="black", fg="white")
    b24.pack()

    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    import numpy as np

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = 'Marks Obtained', 'Total Marks'
    sizes = [int(mark), 5-int(mark)]
    explode = (0.1, 0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels,
                             autopct='%1.1f%%', shadow=True, startangle=0)

    canvas = FigureCanvasTkAgg(fig, master=sh)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    b23 = Button(text="Sign Out", font='Arial 20 bold', command=callsignUpPage,
                 fg="white", bg="black")
    b23.pack()

    sh.mainloop()


def start():
    global root
    root = Tk()
    root.iconbitmap('quiz.ico')
    root.title('Welcome To Quiz Application')
    canvas = Canvas(root, width=1570, height=725, bg='black')
    canvas.grid(column=0, row=1)
    quiz_img = Image.open('quiz.jpg')
    img = ImageTk.PhotoImage(quiz_img)
    canvas.create_image(120, 10, image=img, anchor=NW)

    start_img = Image.open('start.jpg')
    start_btn = ImageTk.PhotoImage(start_img)
    button = Button(root, image=start_btn, command=signUpPage,
                    bg="black", fg="yellow")
    button.configure(width=1570, height=100,
                     activebackground="black", relief=SUNKEN)
    button.grid(column=0, row=2)

    root.mainloop()


if __name__ == '__main__':
    start()
