from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
import os


# Creating Window
root = Tk()
root.geometry('1200x725+100+0')
root.title('Update Client Record - Wadhwa Legal Consultancy System')
root.resizable(False, False)


# Defining Variables
b = StringVar()
c = StringVar()
d = StringVar()
e = StringVar()
f = StringVar()




# Logo
logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)
logo_label.pack()

# Search Button Image
search_img=ImageTk.PhotoImage(Image.open('new-search.png'))

# Heading 
Label(root, text='Update Appointment Record', font=('Romanesco', 34)).place(x=435, y=200)

# First Label
Label(root, text='Enter Appointment ID   :', font=('TimesNewRoman', 16)).place(x=250, y=260)
Label(root, text='WLC / APT / ', font=('TimesNewRoman', 16)).place(x=500, y=260)


# Entry Widget for Client ID
Entry(root, textvariable=b, bd=0, bg='#E2E2E2', font=('TimesNewRoman', 16), width=15).place(x=640, y=263)


# Defining Search Function
def search():
    if len(b.get()) == 0:
        messagebox.showinfo('Error','Please Enter Appointment ID !!!')
    else:    
        conn = sqlite3.connect('wlc_administration_system.db')
        myCursor = conn.cursor()
        myCursor.execute("SELECT * FROM bookings WHERE booking_id = ?",[b.get()])
        pc = myCursor.fetchall()
        myCursor.close()
        conn.close()
        if pc:
            messagebox.showinfo('Success','Appointment Record Found :)')
            for row in pc:
                ent1.insert(0, row[2])
                ent2.insert(0, row[3])
                label1.config(text=row[7])
        else:
            messagebox.showinfo('Oops!','Client Record not Found :(')  

def update():
    if len(c.get()) == 0:
        messagebox.showinfo('Error','Client Name is Required !!!')
    elif len(d.get()) == 0:
        messagebox.showinfo('Error','Client Phone Number is Required !!!')            
    else:    
        if len(e.get()) == 0:
            conn = sqlite3.connect('wlc_administration_system.db')
            myCursor = conn.cursor()
            myCursor.execute("UPDATE bookings SET client_name=?, phone_number=? WHERE booking_id = ?",[c.get(), d.get(), b.get()])
            conn.commit()
            myCursor.close()
            conn.close()
        elif e.get() == 'PAID':
            conn = sqlite3.connect('wlc_administration_system.db')
            myCursor = conn.cursor()
            myCursor.execute("UPDATE bookings SET client_name=?, phone_number=?, fee_status = ?, fee_amount = ? WHERE booking_id = ?",[c.get(), d.get(), e.get(), 'Rs. 2000.00', b.get()])
            conn.commit()
            myCursor.close()
            conn.close()
        elif e.get() == 'NOT PAID':
            conn = sqlite3.connect('wlc_administration_system.db')
            myCursor = conn.cursor()
            myCursor.execute("UPDATE bookings SET client_name=?, phone_number=?, fee_status = ?, fee_amount = ? WHERE booking_id = ?",[c.get(), d.get(), e.get(), 'Rs. 0.00', b.get()])
            conn.commit()
            myCursor.close()
            conn.close()    
        else:
            messagebox.showinfo('Error','Something Went Wrong !!!')
        if True:
            messagebox.showinfo('Success','Client Record Updated Successfully !!!')
            root.destroy()
        else:
            messagebox.showinfo('Error',"Failed to update Client Record !!!")
            root.destroy()



# Body Lables
Label(root, text='Client Name', font=('TimesNewRoman', 16)).place(x=300, y=350)
Label(root, text='Client Phone Number', font=('TimesNewRoman', 16)).place(x=300, y=400)
Label(root, text='Fee Status', font=('TimesNewRoman', 16)).place(x=300, y=450)
Label(root, text='Change Fee Status', font=('TimesNewRoman', 16)).place(x=300, y=500)
label1 = Label(root, font=('TimesNewRoman', 16))
label1.place(x=600, y=450)


# Body Entry
ent1 = Entry(root, textvariable=c, font=('TimesNewRoman', 16), bd=0, bg='#E2E2E2')
ent2 = Entry(root, textvariable=d, font=('TimesNewRoman', 16), bd=0, bg='#E2E2E2')
ent4 = ttk.Combobox(root, textvariable=e, values=('PAID','NOT PAID'), state='readonly', width=37)

ent1.place(x=600, y=350)
ent2.place(x=600, y=400)
ent4.place(x=600, y=500)

# Search Button
Button(root, image=search_img, command=search, bd=0).place(x=850,y=260)

# Button to Update
Button(root, text='Update', font=('TimesNewRoman', 18), bd=0, bg='skyblue', padx=50, command=update).place(x=500, y=600)


root.mainloop()