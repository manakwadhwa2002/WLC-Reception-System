# Importing Required Libraries

from tkinter import *
from tkinter import Tk, Label
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
import os
py=sys.executable

# Creating Window
root = Tk()
root.geometry('1366x786')
root.state('zoomed')
root.title('Admin Dashboard - Wadhwa Legal Consultancy System')# Window Title
root.canvas = Canvas(width=1366, height=768)
root.iconbitmap('favicon.ico') # Logo in the Title Bar
# logo = ImageTk.PhotoImage(Image.open('Logo(300x300).png'))
# logo_label = Label(root, image=logo)

# Defining Functions

def add_apt():
    os.system('%s %s' % (py, 'add_appointment_record.py'))
def book():
    os.system('%s %s' % (py, 'book_appointment.py'))
def find_apt():
    os.system('%s %s' % (py, 'find_appointment.py'))
def add_client():
    os.system('%s %s' % (py, 'reg_new_client.py'))
def update_clt_rcd():
    os.system('%s %s' % (py, 'update_client_record.py'))   
def find_client():
    os.system('%s %s' % (py, 'find_client.py'))
def update_apt_rcd():
    os.system('%s %s' % (py, 'update_apt_record.py'))
def print_inv(): # To Be Done
    os.system('%s %s' % (py, 'main.py'))
def today_apts():
    os.system('%s %s' % (py, 'today_appointments.py'))    
def logout():
    messagebox.showwarning('Warning','You will be logged out of the system !!!')
    ask = messagebox.askyesno('Logout','Do you want to logout ?')
    if ask:
        root.destroy()    

# Labels 

logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
Label(root, image=logo).place(x=10, y=10)
Label(root, text='Dashboard', font=('Roboto', 50, 'bold')).place(x=275, y=75)

logout_img = ImageTk.PhotoImage(Image.open('LogoutNew.png'))
Button(root, image=logout_img, font=('TimesNewRoman', 16, 'bold'), bd=0, command=logout).place(x=1290, y=25)

# Row 1
Button(root, text='Add Appointment Record', font=('TimesNewRoman', 16), bd=0, bg='#E4E4E4', fg='black', padx=50, pady=12, command=add_apt).place(x=50, y=300)
Button(root, text='Book New Appointment', font=('TimesNewRoman', 16), bd=0, bg='orangered', fg='black', padx=50, pady=12, command=book).place(x=525, y=300)
Button(root, text='Find Appointment', font=('TimesNewRoman', 16), bd=0, bg='grey', fg='black', padx=75, pady=12, command=find_apt).place(x=1000, y=300)

# Row 2
Button(root, text='Add New Client', font=('TimesNewRoman', 16), bd=0, bg='#003862', fg='white', padx=93, pady=12, command=add_client).place(x=50, y=450)
Button(root, text='Update Client Record', font=('TimesNewRoman', 16), bd=0, bg='lightgreen', fg='black', padx=60, pady=12, command=update_clt_rcd).place(x=525, y=450)
Button(root, text='Find Client', font=('TimesNewRoman', 16), bd=0, bg='skyblue', fg='black', padx=105, pady=12, command=find_client).place(x=1000, y=450)

# Row 3
Button(root, text='Update Appointment Record', font=('TimesNewRoman', 16), bd=0, bg='orange', fg='black', padx=35, pady=12, command=update_apt_rcd).place(x=50, y=600)
Button(root, text='Print Invoice', font=('TimesNewRoman', 16), bd=0, bg='black', fg='white', padx=100, pady=12, command=print_inv).place(x=525, y=600)
Button(root, text='Today(s) Appointments', font=('TimesNewRoman', 16), bd=0, bg='yellow', fg='black', padx=45, pady=12, command=today_apts).place(x=1000, y=600)

root.mainloop()