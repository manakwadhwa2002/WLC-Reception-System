# Importing Required Libraries

from tkinter import *
from tkinter import Tk, Label
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
import os
py=sys.executable

# Creating  Window
root = Tk()
root.geometry('1366x786')
root.state('zoomed')
root.title('Admin Login - Wadhwa Legal Consultancy System')# Window Title
root.canvas = Canvas(width=1366, height=768)
root.iconbitmap('favicon.ico') # Logo in the Title Bar
logo = ImageTk.PhotoImage(Image.open('Logo(300x300).png'))
logo_label = Label(root, image=logo)
a = StringVar()
b = StringVar()

# Defining Functions

def login():
    if(len(a.get())) == 0:
        messagebox.showinfo('Error',"Nothing in Username")
    elif(len(b.get())) == 0:
        messagebox.showinfo('Error',"Nothing in Password")
    else:
        try:
            conn = sqlite3.connect('wlc_administration_system.db')
            myCursor = conn.cursor()
            myCursor.execute("SELECT * FROM admin WHERE username=? AND password=?", [a.get(), b.get()])
            pc = myCursor.fetchall()
            myCursor.close()
            conn.close()
            if pc:
                messagebox.showinfo('Welcome', 'Welcome, You are authenticated :)')
                root.destroy()
                os.system('%s %s' % (py, 'admin_dashboard.py'))
            else:
                messagebox.showinfo('Error', 'Username and password not found :(')
        except:
            messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

# Creating Widgets

logo_label.pack()
Label(root, text='ADMIN LOGIN', font=('Verdana', 25)).place(x=580, y=280)
Label(root, text='Username :', font=('Raleway', 25)).place(x=365, y=350)
Label(root, text='Password :', font=('Raleway', 25)).place(x=365, y=450)
Entry(root, textvariable=a, font=('Romanesco', 25), bd=0, bg="#E2E2E2", width=45).place(x=600, y=355)
Entry(root, textvariable=b, font=('Romanesco', 25), bd=0, bg="#E2E2E2", width=45, show="*").place(x=600, y=455)
Button(root, text="Login", command=login, width='18', font=('Verdana', 15, 'bold', 'italic'), bd=0, bg='skyblue').place(x=420, y=545)
Button(root, text='Forgot Password ?', width='18', font=('Verdana', 15, 'bold', 'italic'), bd=0, bg='orangered').place(x=770, y=545)

# Company Label
Label(root, text="Manak Wadhwa | © Copyright 2020 - Wadhwa Legal Consultancy", font=('Verdana', 11, 'bold')).place(x=475, y=660)

root.mainloop()