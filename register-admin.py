from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import os,sys
py=sys.executable

root = Tk()
root.geometry('1366x786')
root.state('zoomed')
root.title('Admin Register - Wadhwa Legal Consultancy System')# Window Title
root.canvas = Canvas(width=1366, height=768)
root.iconbitmap('favicon.ico') # Logo in the Title Bar
logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)


# Defining Text Variables
c = StringVar()
d = StringVar()
e = StringVar()
f = StringVar()
g = StringVar()
h = StringVar()
j = StringVar()
k = StringVar()
l = StringVar()
m = StringVar()

# Create Table if not created

conn = sqlite3.connect('wlc_administration_system.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS admin
(
	username	TEXT,
	first_name	TEXT,
	last_name	TEXT,
	password	TEXT,
	secQuestion	TEXT,
	secAnswer	TEXT,
	Phone	TEXT,
	Address	TEXT,
	City	TEXT,
	zipcode	TEXT
) '''
)
conn.commit()



# Defining Functions

def insert():
    conn = sqlite3.connect('wlc_administration_system.db')
    with conn:
        myCursor = conn.cursor()
        myCursor.execute("INSERT INTO admin(username, first_name, last_name, password, secQuestion, secAnswer, Phone, Address, City, zipcode)")
        if True:
            messagebox.showinfo('Success','Admin Created Successfully ! :)')
            root.destroy()
        else:
            messagebox.showinfo('Error','Something Went Wrong.\nPlease try again :(')    
   

def verify():
    if len(c.get()) == 0:
        messagebox.showinfo('Error','Username is Required !!!')
    elif len(d.get()) == 0:
        messagebox.showinfo('Error','First Name is Required !!!')
    elif len(e.get()) == 0:
        messagebox.showinfo('Error','Last Name is Required !!!')
    elif len(l.get()) == 0:
        messagebox.showinfo('Error','City is Required !!!')        
    elif len(k.get()) == 0:
        messagebox.showinfo('Error','Address is Required !!!')
    elif len(m.get()) != 6:
        messagebox.showinfo('Error','Pincode is Required !!!')
    elif len(g.get()) == 0:
        messagebox.showinfo('Error','Security Question is Required !!!')    
    elif len(h.get()) == 0:
        messagebox.showinfo('Error','Security Answer is Required !!!')
    elif len(f.get()) == 0:
        messagebox.showinfo('Error','Password is Required !!!')
        '''
    elif len(f.get()) < 8:
           while True:
                if not re.search("[a-z]", f.get()):
                   messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
                   break
                elif not re.search("[A-Z]", f.get()):
                    messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
                    break
                elif not re.search("[0-9]", f.get()):
                    messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
                    break
                elif not re.search("[_@$]", f.get()):
                    messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
                    break
                elif not re.search("\s", f.get()):
                    messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
                    break
                else:
                    break
                '''
    elif len(j.get()) == 0:
        messagebox.showinfo('Error','Phone Number is Required !!!')        
    elif len(j.get()) != 10:
        messagebox.showinfo('Error','Phone Number Must be 10 digits') 
    else:
        insert()        


def cancel():
    root.destroy()

# Creating Widgets Lables
Label(root, text='ADMIN REGISTER', font=('Verdana, 30')).place(x=500, y=220)
# For 150
Label(root, text='Username', font=('Verdana, 20')).place(x=150, y=330)
Label(root, text='First Name', font=('Verdana, 20')).place(x=150, y=390)
Label(root, text='Last Name', font=('Verdana, 20')).place(x=150, y=440)
Label(root, text='Phone', font=('Verdana, 20')).place(x=150, y=490)
Label(root, text='City', font=('Verdana, 20')).place(x=150, y=540)

# For 750
Label(root, text='Address', font=('Verdana, 20')).place(x=750, y=330)
Label(root, text='Pincode', font=('Verdana, 20')).place(x=750, y=390)
Label(root, text='Security Question', font=('Verdana, 20')).place(x=750, y=440)
Label(root, text='Security Answer', font=('Verdana, 20')).place(x=750, y=490)
Label(root, text='Password', font=('Verdana, 20')).place(x=750, y=540)

# Creating Widgets Entry
# For 350
Entry(root, textvariable='c', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=350, y=330)
Entry(root, textvariable='d', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=350, y=390)
Entry(root, textvariable='e', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=350, y=440)
Entry(root, textvariable='j', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=350, y=490)
Entry(root, textvariable='l', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=350, y=540)

# For 1000
Entry(root, textvariable='k', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=1000, y=330)
Entry(root, textvariable='m', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=1000, y=390)
ttk.Combobox(root, textvariable='g', values=["What is your school name?", "What is your home name?","What is your Father name?", "What is your pet name?"], width=46,state="readonly").place(x=1000, y=440)
Entry(root, textvariable='h', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=1000, y=490)
Entry(root, textvariable='f', font=('TimesNewRoman, 20'), bd=0, bg="#E2E2E2").place(x=1000, y=540)

# Creating Buttons

Button(root, text='Create Admin', bg='skyblue', width=25, font=('Roboto, 14'), bd=0, command=verify).place(x=415, y=625)
Button(root, text='Cancel', bg='red',fg='white', width=25, font=('Roboto, 14'), bd=0, command=cancel).place(x=815, y=625)

# Company Label
Label(root, text="Manak Wadhwa | © Copyright 2020 - Wadhwa Legal Consultancy", font=('Verdana', 11, 'bold')).place(x=475, y=680)

logo_label.pack()



root.mainloop()
