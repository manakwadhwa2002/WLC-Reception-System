from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import sqlite3
import os, sys


# Creating Window
root = Tk()
root.geometry('1250x700+60+0')
root.title('Add Appointment Record - Wadhwa Legal Consultancy System')
root.iconbitmap('favicon.ico')
root.resizable(False, False)


# Defining Variables
e = StringVar()
f = StringVar()
g = StringVar()
h = StringVar()
i = StringVar()
j = StringVar()
k = StringVar()
l = StringVar()
m = StringVar()
p = StringVar()


# Defining Functions
def verify():
    if len(e.get()) == 0:
        messagebox.showinfo('Error','Please Enter Client ID !!!')
    elif len(f.get()) == 0:
        messagebox.showinfo('Error','Please Enter Client Phone Number !!!')
    elif len(f.get()) != 10:
        messagebox.showinfo('Error','Please Check Client Phone Number !!!')
    elif len(g.get()) == 0:
        messagebox.showinfo('Error','Please Select a time slot !!!')
    elif len(h.get()) == 0:
        messagebox.showinfo('Error','Please set fee status !!!')
    elif len(i.get()) == 0:
        messagebox.showinfo('Error','Please Enter Client Name !!!')
    elif len(j.get()) == 0:
        messagebox.showinfo('Error','Please Select a Day !!!')    
    elif len(k.get()) == 0:
        messagebox.showinfo('Error','Please Select a Month !!!')        
    elif len(l.get()) == 0:
        messagebox.showinfo('Error','Please Select a Date !!!')    
    elif len(m.get()) == 0:
        messagebox.showinfo('Error','Please Select a Year !!!')    
    elif len(p.get()) == 0:
        messagebox.showinfo('Error','Please Select a Consultant !!!')            
    else:
        find()

def find():
    ent7 = j.get()+', '+l.get()+' '+k.get()+' '+m.get()

    conn = sqlite3.connect('wlc_administration_system.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookings WHERE date=? AND time_slot=?", [ent7, g.get()])
    aal = cur.fetchall()
    cur.close()
    conn.close()
    if aal:
        messagebox.showinfo('Oops!','We already have an Appointment .\n Please Try to Book in some other slot !')
    else:
        messagebox.showinfo('Success','You can Book Appointement in this slot :)')
        insert()

def insert():
    ent1 = alfa
    ent2 = e.get()
    ent3 = f.get()
    ent4 = g.get()
    ent5 = h.get()
    ent6 = i.get()
    ent7 = j.get()+', '+l.get()+' '+k.get()+' '+m.get()
    ent8 = p.get()
    ent9 = 'Rs. 2000.00'
    ent10 = beta
    ent11 = 'Rs. 0.00'
    ent12 = '0'
    if h.get() == 'PAID':
        conn = sqlite3.connect('wlc_administration_system.db')
        myCursor = conn.cursor()
        myCursor.execute('INSERT INTO bookings(booking_id, client_id, client_name, phone_number, date, time_slot, consultant_name, fee_status, fee_amount, invoice_num) VALUES(?,?,?,?,?,?,?,?,?,?)',(ent1, ent2, ent6, ent3, ent7, ent4, ent8, ent5, ent9, ent10,))
        conn.commit()
        if True:
            messagebox.showinfo('Success','Appointment Record Added Successfully :)')
            ask = messagebox.askyesno('Add Another','Do you want to add another Appointment Record !!!')
            if ask:
                root.destroy()
                os.system('%s %s' % (py, 'add_appointment_record.py'))
            else:
                root.destroy()   
        else:
            messagebox.showinfo('Error','Failed to add Appointment Record :(')
    elif h.get() == 'NOT PAID':
        conn = sqlite3.connect('wlc_administration_system.db')
        myCursor = conn.cursor()
        myCursor.execute('INSERT INTO bookings(booking_id, client_id, client_name, phone_number, date, time_slot, consultant_name, fee_status, fee_amount, invoice_num) VALUES(?,?,?,?,?,?,?,?,?,?)',(ent1, ent2, ent6, ent3, ent7, ent4, ent8, ent5, ent11, ent12))
        conn.commit()
        if True:
            messagebox.showinfo('Success','Appointment Record Added Successfully :)')
            ask = messagebox.askyesno('Add Another','Do you want to add another Appointment Record !!!')
            if ask:
                root.destroy()
                os.system('%s %s' % (py, 'add_appointment_record.py'))
            else:
                root.destroy()
        else:
            messagebox.showinfo('Error','Failed to add Appointment Record :(')
    else:
        messagebox.showinfo('Error','Something Went Wrong :(')



# Logo
logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)
logo_label.pack()


# Heading
Label(root, text='Add Appointment Record', font=('Romanesco', 32)).pack()


# Appointment ID Label (Fixed)
Label(root, text='Appointment ID  :', font=('TimesNewRoman', 18)).place(x=400, y=300)
Label(root, text='WLC / APT / ', font=('TimesNewRoman', 18)).place(x=600, y=300)
label1 = Label(root, font=('TimesNewRoman', 18))
label1.place(x=740, y=300)


# Lables (100)
Label(root, text='Client ID', font=('TimesNewRoman', 16)).place(x=150, y=350)
Label(root, text='Client Ph. No', font=('TimesNewRoman', 16)).place(x=150, y=400)
Label(root, text='Time Slot', font=('TimesNewRoman', 16)).place(x=150, y=450)
Label(root, text='Fee Status', font=('TimesNewRoman', 16)).place(x=150, y=500)


# Lables (700)
Label(root, text='Client Name', font=('TimesNewRoman', 16)).place(x=700, y=350)
Label(root, text='Date', font=('TimesNewRoman', 16)).place(x=700, y=400)
Label(root, text='Consultant Name', font=('TimesNewRoman', 16)).place(x=700, y=450)


# Entry & Combobox Widgets (375)
Entry(root, textvariable=e, font=('TimesNewRoman', 16), bd=0, bg='#E2E2E2').place(x=375, y=350)
Entry(root, textvariable=f, font=('TimesNewRoman', 16), bd=0, bg='#E2E2E2').place(x=375, y=400)
ttk.Combobox(root, textvariable=g, values=["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM", "06:00 PM", "07:00 PM", "08:00 PM"], width=37,state="readonly").place(x=375, y=450)
ttk.Combobox(root, textvariable=h, values=["PAID", "NOT PAID"], width=37,state="readonly").place(x=375, y=500)


# Entry & Combobox Widgets (375)
Entry(root, textvariable=i, font=('TimesNewRoman', 16), bd=0, bg='#E2E2E2').place(x=925, y=350)
# Date
ttk.Combobox(root, textvariable=j, values=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], width=5,state="readonly").place(x=925, y=400)
ttk.Combobox(root, textvariable=k, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Aug", "Sep", "Oct", "Nov", "Dec"], width=5,state="readonly").place(x=990, y=400)
ttk.Combobox(root, textvariable=l, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"], width=5,state="readonly").place(x=1055, y=400)
ttk.Combobox(root, textvariable=m, values=["2020", "2021", "2022", "2023", "2024", "2025"], width=5,state="readonly").place(x=1120, y=400)

ttk.Combobox(root, textvariable=p, values=["Sr. Adv. Vinod Wadhwa", "Prof. OP Wadhwa"], width=37,state="readonly").place(x=925, y=450)


# Add Button
Button(root, text='Add Appointment', font=('TimesNewRoman', 18), bd=0, bg='skyblue',padx=20, command=verify).place(x=550, y=560)


# Copyright Label
Label(root, text="Manak Wadhwa | © Copyright 2020 - Wadhwa Legal Consultancy", font=('Verdana', 11, 'bold')).place(x=375, y=655)


# Booking Empty list
booking_id_list = []



# Fetching Data from Database for Unique Id
conn = sqlite3.connect('wlc_administration_system.db') 
myCursor = conn.cursor()
myCursor.execute('SELECT booking_id from bookings')
pc = myCursor.fetchall()
myCursor.close()
conn.close()


# Making a integer list of all the numbers in Booking ID
for aad in pc:
    for aaf in aad:
        booking_id_list.append(int(aaf))

# Defining Unique Id Function
def id():
    z = 0
    while z < 1000000:
        n = random.randint(1, 999999)
        if n in booking_id_list:
            z += 1
        else:
            z = z
            break
    return n 

alfa = id()            

# Invoice Empty List
invoice_list = []


# Fetching Data from Database for Invoice Number
conn = sqlite3.connect('wlc_administration_system.db') 
myCursor = conn.cursor()
myCursor.execute('SELECT invoice_num from bookings')
cp = myCursor.fetchall()
myCursor.close()
conn.close()


# Making a integer list of all the numbers in Invoice Number
for ghj in cp:
    for hjk in ghj:
        invoice_list.append(int(hjk))

# Defining Unique Invoice ID Function
def invo_id():
    x = 0
    while x < 1000000000:
        y = random.randint(1, 999999999)
        if y in invoice_list:
            x += 1
        else:
            x = x
            break
    return y        



beta = invo_id()

# Placing n in label1

def replace():
    label1.config(text=str(alfa))

replace()


root.mainloop()


#Wed, 03 Feb 2021